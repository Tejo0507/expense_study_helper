# Smart Expense Categorizer & Study Plan Generator

This project is a Streamlit-based web app combining two intelligent modules designed to make daily life easier and more organized.

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
   `git clone <repo-url>`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the app  
   `python -m streamlit run app/main.py`

