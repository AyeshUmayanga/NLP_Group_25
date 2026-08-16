# NLP Group 25 - Fake News Detection

## 📌 Project Overview

This project is a Natural Language Processing (NLP) based Fake News Detection system developed for the CCS3356 Natural Language Processing group assignment.

The system analyzes news article text and classifies it as:

- **Fake News**
- **Real News**

The project implements different machine learning and deep learning approaches and compares their performance to identify the most suitable model for the final application.

---

## 👥 Group Members

| Student ID | Name | Model |
|------------|------|-------|
| CIT-24-01-0458 | Vihanga Sathsarani | SVM |
| Student ID | Member 2 | Model |
| Student ID | Member 3 | Model |

---

## 🎯 Problem Statement

The rapid spread of misinformation through online news platforms has become a major challenge.

The objective of this project is to develop an NLP-based automated system that can identify whether a given news article is **Fake** or **Real** based on its textual content.

---

## 📊 Dataset

The project uses a labelled news dataset containing both fake and real news articles.

### Dataset Contains

- News title
- News article text
- News category/label

### Target Classes

- `Fake`
- `Real`

The dataset is preprocessed before model training to remove unnecessary text and prepare the data for NLP-based feature extraction and modelling.

---

## 🔄 NLP Pipeline

The project follows the following NLP pipeline:

```text
Raw News Dataset
        ↓
Data Cleaning
        ↓
Text Preprocessing
        ↓
Tokenization
        ↓
Stopword Removal
        ↓
Feature Extraction
        ↓
Train / Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Fake / Real Prediction
