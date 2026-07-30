# NLP_Group_25
# Fake News Detection using Machine Learning

## Project Overview

This project focuses on detecting fake news articles using Natural Language Processing (NLP) and Machine Learning techniques. The news articles are preprocessed, transformed into numerical features using TF-IDF Vectorization, and classified using multiple machine learning algorithms.

## Team Members

| Member | Task |
|---------|------|
| Member 1 | Data Loading, Exploratory Data Analysis (EDA), Text Preprocessing, Logistic Regression | Bert
| Member 2 | Support Vector Machine (SVM) | LSTM
| Member 3 | Random Forest | GRU

## Dataset

The project uses two datasets:

- Fake.csv
- True.csv

The datasets were merged and labelled:
- Fake News → 0
- True News → 1

Total Records: **44,898**

## Project Structure

```
## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib

## Machine Learning Models

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

## Text Preprocessing

- Lowercase Conversion
- URL Removal
- Punctuation Removal
- Number Removal
- Tokenization
- Stopword Removal
- Lemmatization
- TF-IDF Vectorization

## Logistic Regression Performance

Accuracy: **99%**

Classification Report

| Metric | Class 0 | Class 1 |
|---------|---------|---------|
| Precision | 0.99 | 0.98 |
| Recall | 0.98 | 0.99 |
| F1-Score | 0.99 | 0.99 |

## Future Improvements

- Deep Learning Models
- BERT
- RoBERTa
- Real-time Fake News Detection
