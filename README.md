# NLP Group 25 – Fake News Detection

## Project Overview

This project is an NLP-based Fake News Detection system developed for the **CCS3356 – Natural Language Processing** module at Sri Lanka Technology Campus.

The system applies Natural Language Processing, Machine Learning, and Deep Learning techniques to classify news articles as **Fake** or **True**.

## Problem Statement

Fake news can spread rapidly through online platforms and mislead the public. This project aims to develop an NLP-based system that analyzes news content and predicts whether the given news is Fake or True.

## Project Objectives

- Collect and prepare a real-world news dataset
- Perform text preprocessing and exploratory data analysis
- Apply suitable NLP feature representation techniques
- Develop Machine Learning and Deep Learning models
- Evaluate and compare the developed models
- Develop a functional Fake News Detection application
- Identify ethical issues, dataset bias, and responsible AI concerns

## Dataset

The project uses a real-world Fake News dataset containing news articles categorized as Fake or True.

The original dataset contains the following features:

- Title
- Text
- Subject
- Date

After data cleaning and preprocessing, the final dataset contains **39,105 records**.

The target labels are:

- `0` – Fake News
- `1` – True News

## NLP Pipeline

The project follows a complete NLP pipeline consisting of:

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering and Text Representation
5. Model Development
6. Model Training
7. Model Evaluation
8. Model Comparison
9. Final Application Development

## Group Members and Model Allocation

| Student ID | Machine Learning Model | Deep Learning Model |
|---|---|---|
| cit-24-01-0535 | Logistic Regression | BERT |
| cit-24-01-0458 | SVM | LSTM |
| cit-24-01-0534 | Random Forest | GRU |

Each member independently developed one Machine Learning model and one Deep Learning model using the same dataset and problem domain.

### Member 1 Contribution – cit-24-01-0535

Member 1 independently developed and evaluated the following models:

**Machine Learning Model – Logistic Regression**

- TF-IDF was used for text feature extraction
- Stratified train-test splitting was applied
- The model was trained using the cleaned news text
- Performance was evaluated using standard classification metrics

**Deep Learning Model – BERT**

- Pre-trained `bert-base-uncased` was used
- BERT tokenization was applied to the news text
- The model was fine-tuned for binary classification
- Performance was evaluated using standard classification metrics

## Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 98.76% | 98.50% | 99.22% | 98.86% | N/A |
| SVM | 99.37% | 99.25% | 99.60% | 99.42% | 99.93% |
| Random Forest | 99.65% | 99.55% | 99.81% | 99.68% | 99.95% |
| BERT | 99.31% | 98.76% | 99.98% | 99.37% | 99.98% |
| LSTM | 98.71% | 98.48% | 99.15% | 98.81% | 99.79% |
| GRU | 99.72% | 99.60% | 99.88% | 99.74% | 99.96% |

## Evaluation Metrics

The developed models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC

The performance of all six models is compared to identify the most suitable model for the final application.

## Final Application

After evaluating all six models, the most suitable model will be selected for integration into the final Fake News Detection application.

The application will provide a user-friendly interface where users can enter news content and receive a prediction indicating whether the content is likely to be Fake or True.

## Ethics and Responsible AI

The project considers several ethical and responsible AI aspects, including:

- Dataset bias
- Fairness
- False positive and false negative predictions
- Potential harmful outputs
- Privacy considerations
- Limitations of automated news classification

The system is intended to support users in analyzing news content and should not be considered an absolute authority for determining factual truth.

## Project Structure

```
NLP_Group_25/
│
├── data/
├── notebooks/
├── src/
├── models/
├── reports/
├── screenshots/
├── videos/
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- Keras
- PyTorch
- Hugging Face Transformers
- Jupyter Notebook
- Git
- GitHub
- Streamlit

## Setup

Clone the repository:

```bash
git clone https://github.com/AyeshUmayanga/NLP_Group_25.git
```

Navigate to the project directory:

```bash
cd NLP_Group_25
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Navigate to the `notebooks/` directory.
4. Open the required Jupyter Notebook.
5. Run the preprocessing and model development steps.
6. Evaluate the trained model.
7. Run the final application from the `src/` directory.

## Project Workflow

```
Dataset
   ↓
Data Cleaning
   ↓
Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Best Model Selection
   ↓
Final Application
```

## Academic Information

- **Module:** CCS3356 – Natural Language Processing
- **Institution:** Sri Lanka Technology Campus
- **Project:** Group Assignment – Fake News Detection
- **Group:** NLP Group 25
