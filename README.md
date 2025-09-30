# Smart Expense Categorizer & Study Plan Generator

This project is a Streamlit app using ML techniques like sentence embeddings and logistic regression for smart expense categorization and personalized study planning.

## Features

### 1. Expense Categorizer
- Converts transaction SMS texts into vector embeddings using Sentence Transformers for semantic understanding.
- Utilizes Logistic Regression to classify expenses into categories like Food, Travel, Shopping, Bills, Entertainment, and Others.
- Provides an easy-to-use interface to input transaction texts and view predictions with visual charts of expense distribution.
- Includes realistic labeled datasets for training and testing.

### 2. Study Plan Generator
- Accepts inputs such as total study hours, subject list, upcoming exam dates, and marks weak/strong subjects.
- Implements a prioritization algorithm to allocate study hours efficiently, focusing more on weak subjects and near exams.
- Outputs a clear, balanced daily study schedule to help users prepare effectively.

## Project Structure and File Descriptions

- **app/main.py**  
  Main Streamlit app frontend managing UI, user inputs, and displaying categorized expenses and study plans via interactive tabs.

- **modules/utils.py**  
  Shared utility functions for text cleaning, exam date parsing, and subject list validation to support other modules.

- **modules/expense.py**  
  Implements ML pipeline for expense classification: dataset processing, embedding generation (Sentence Transformers), model training (Logistic Regression), and prediction.

- **modules/study_plan.py**  
  Generates personalized study plans considering available study hours, subjects, exams, and strengths/weaknesses for effective scheduling.

- **models/**  
  Stores serialized trained models (`expense_classifier_emb.pkl`, `embedder.pkl`) loaded by the app for inference.

- **requirements.txt**  
  Lists Python package dependencies for reproducible setup and deployment.

This modular design separates core ML and logic from the UI for clean, maintainable, and scalable development.

## Installation & Usage

1. Clone the repository  
   `git clone https://github.com/Tejo0507/expense_study_helper.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the app  
   `python -m streamlit run app/main.py`

<img width="1863" height="1005" alt="image" src="https://github.com/user-attachments/assets/13d8c64a-1e81-473a-be34-6073076dee1a" />
<img width="1826" height="992" alt="image" src="https://github.com/user-attachments/assets/a50f93b6-4ee7-40d4-be80-de67d93cb8e2" />
<img width="1857" height="1007" alt="image" src="https://github.com/user-attachments/assets/37a37941-bb76-4fb6-9f63-f684eb49fa71" />
<img width="1861" height="1001" alt="image" src="https://github.com/user-attachments/assets/ff8680c2-bc38-41ed-b2b1-dc68da6eb633" />
