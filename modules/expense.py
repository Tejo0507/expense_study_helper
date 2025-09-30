import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from sentence_transformers import SentenceTransformer
import numpy as np
import os
from modules.utils import clean_text

data = [
    ("Swiggy 250", "Food"),
    ("Zomato order 399", "Food"),
    ("Dominos 500", "Food"),
    ("McDonalds 220", "Food"),
    ("Cafe Coffee Day 170", "Food"),
    ("Uber 300", "Travel"),
    ("Ola Cab 340", "Travel"),
    ("IRCTC 1250", "Travel"),
    ("Flight Indigo 4500", "Travel"),
    ("KSRTC Bus 500", "Travel"),
    ("Amazon 899", "Shopping"),
    ("Flipkart 1999", "Shopping"),
    ("Myntra 525", "Shopping"),
    ("Lifestyle 1100", "Shopping"),
    ("Big Bazaar 700", "Shopping"),
    ("Airtel Bill 499", "Bills"),
    ("Electricity 1800", "Bills"),
    ("Water Bill 300", "Bills"),
    ("Jio recharge 239", "Bills"),
    ("Gas Bill 700", "Bills"),
    ("Netflix 499", "Entertainment"),
    ("PVR Cinemas 350", "Entertainment"),
    ("Spotify 119", "Entertainment"),
    ("BookMyShow 699", "Entertainment"),
    ("Hotstar 299", "Entertainment"),
    ("Axis Bank Credit Card payment 9800", "Others"),
    ("LIC Premium 1500", "Others"),
    ("Donation Goonj 250", "Others"),
    ("Gold purchase 12000", "Others"),
    ("ATM Withdrawal 2000", "Others"),
]

df = pd.DataFrame(data, columns=["text", "category"])

df['clean_text'] = df['text'].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], df['category'], test_size=0.3, random_state=42, stratify=df['category']
)

embedder = SentenceTransformer('all-MiniLM-L6-v2')

X_train_emb = embedder.encode(X_train.to_list(), convert_to_numpy=True)
X_test_emb = embedder.encode(X_test.to_list(), convert_to_numpy=True)

clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train_emb, y_train)

y_pred = clf.predict(X_test_emb)
print(classification_report(y_test, y_pred))

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
models_dir = os.path.join(project_root, "models")
os.makedirs(models_dir, exist_ok=True)

joblib.dump(clf, os.path.join(models_dir, "expense_classifier_emb.pkl"))
joblib.dump(embedder, os.path.join(models_dir, "embedder.pkl"))

def predict_category(transaction_text):
    processed = clean_text(transaction_text)
    emb = embedder.encode([processed], convert_to_numpy=True)
    return clf.predict(emb)[0]

if __name__ == "__main__":
    print(predict_category("Uber ride 180"))
    print(predict_category("Big Bazaar 650"))
