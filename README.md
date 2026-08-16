# Fake News Detection - Machine Learning & Deep Learning

This folder contains the implementation of **Random Forest (Machine Learning)** and **Gated Recurrent Unit (GRU) (Deep Learning)** models for detecting fake news. This work is part of the NLP project for student/member ID: **cit-24-01-0534**.

Both models have been evaluated on a large news dataset, achieving state-of-the-art performance in classifying news articles as either **True** or **Fake**.

---

## 📂 Project Structure

```directory
cit-24-01-0534/
│
├── data/
│   └── clean_news_dataset.csv                      # Preprocessed news dataset (tracked via Git LFS)
│
├── models/
│   ├── random_forest_model.pkl                      # Trained Random Forest classifier (tracked via Git LFS)
│   ├── random_forest_tfidf_vectorizer.pkl           # TF-IDF Vectorizer for Random Forest
│   ├── gru_model.keras                             # Trained GRU model file (tracked via Git LFS)
│   └── gru_tokenizer.pkl                           # Tokenizer for GRU preprocessing
│
├── results/
│   ├── random_forest_results.csv                   # Classification metrics for Random Forest
│   └── gru_results.csv                             # Classification metrics for GRU
│
├── Random_Forest.ipynb                             # Jupyter notebook for Random Forest training & evaluation
├── GRU.ipynb                                       # Jupyter notebook for GRU training & evaluation
├── .gitignore                                      # Git ignore rules for the workspace
└── .gitattributes                                  # Git LFS configurations for large data and model files
```

---

## 📊 Dataset Overview

* **Dataset Name:** `clean_news_dataset.csv`
* **Total Samples:** 39,105 news articles
* **Target Classes:** 
  * `0` - Fake News
  * `1` - True News
* **Features Used:** 
  * `clean_text` (cleaned textual content of the articles)
  * `label` (binary classification label)

---

## 🤖 Models Implementation

### 1. Random Forest Classifier (`Random_Forest.ipynb`)
The Random Forest model leverages traditional NLP techniques coupled with ensemble learning.
* **Text Representation:** TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer
  * `max_features = 5000`
  * `ngram_range = (1, 2)` (Unigrams & Bigrams)
* **Model Parameters:** `n_estimators = 100`, `n_jobs = -1` for parallel processing.
* **Train/Test Split:** 80% Train, 20% Test (Stratified Split)

### 2. Gated Recurrent Unit (GRU) Network (`GRU.ipynb`)
The GRU model is a sequence-based recurrent neural network (RNN) capable of capturing long-term dependencies in text.
* **Text Representation:** Word Tokenization & Sequence Padding
  * `max_words = 20000` (Vocabulary size)
  * `max_len = 500` (Sequence length)
* **Architecture:**
  * **Embedding Layer:** Input Dimension = 20,000, Output Dimension = 128
  * **GRU Layer:** 64 recurrent units
  * **Dropout Layer:** rate = 0.5 (for regularization)
  * **Dense Output Layer:** 1 unit with Sigmoid activation function
* **Training Hyperparameters:**
  * **Optimizer:** Adam
  * **Loss Function:** Binary Cross-Entropy
  * **Callbacks:** Early Stopping (patience = 2, restoring best weights)

---

## 📈 Performance & Results

Below is the comparison of the two models based on the test split:

| Model Name | Accuracy | Precision | Recall | F1-Score | ROC AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Forest** | 99.65% | 99.55% | 99.81% | 99.68% | 99.95% |
| **GRU (Deep Learning)** | **99.72%** | **99.60%** | **99.88%** | **99.74%** | **99.96%** |

Both models show exceptional accuracy, with the GRU model slightly outperforming the Random Forest model across all classification metrics.

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have the following installed:
* Python 3.8+
* Jupyter Notebook / Google Colab
* Git & Git LFS (Large File Storage)

### Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/AyeshUmayanga/NLP_Group_25.git
   cd NLP_Group_25
   git checkout feature/cit-24-01-0534-Random-forest
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebooks:
   * To train or evaluate Random Forest, open `Random_Forest.ipynb`.
   * To train or evaluate GRU, open `GRU.ipynb`.
