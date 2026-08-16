import streamlit as st
import pickle
import numpy as np
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LEN = 500

@st.cache_resource
def load_gru_model():
    model = load_model("models/gru_model.keras")
    with open("models/gru_tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

st.sidebar.title("About")
st.sidebar.info(
    "**NLP Group 25**\n\n"
    "Fake News Detection System\n\n"
    "Module: CCS3356 – Natural Language Processing\n\n"
    "Institution: Sri Lanka Technology Campus"
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Group Members**")
st.sidebar.markdown(
    "- cit-24-01-0535 — Logistic Regression & BERT\n"
    "- cit-24-01-0458 — SVM & LSTM\n"
    "- cit-24-01-0534 — Random Forest & GRU"
)

model, tokenizer = load_gru_model()

st.title("📰 Fake News Detection")
st.markdown(
    "Enter a news article below to detect whether it is **Fake** or **Real**."
)
st.markdown("---")

title = st.text_input("News Title", placeholder="Enter the headline of the news article")
text = st.text_area("News Text", height=250, placeholder="Paste or type the full news article here")

st.markdown("")

if st.button("🔍 Detect News", use_container_width=True):
    if not title.strip() and not text.strip():
        st.warning("⚠️ Please enter a news title or news text before detection.")
    else:
        combined = f"{title.strip()} {text.strip()}".strip()
        clean = combined.lower()
        clean = re.sub(r"[^a-z\s]", "", clean)
        clean = re.sub(r"\s+", " ", clean).strip()

        sequence = tokenizer.texts_to_sequences([clean])
        padded = pad_sequences(sequence, maxlen=MAX_LEN, padding="post", truncating="post")

        probability = model.predict(padded, verbose=0)[0][0]
        prediction = int(probability >= 0.5)

        st.markdown("---")

        if prediction == 1:
            confidence = probability * 100
            st.success(f"✅ **REAL NEWS** — Confidence: {confidence:.2f}%")
        else:
            confidence = (1 - probability) * 100
            st.error(f"🚨 **FAKE NEWS** — Confidence: {confidence:.2f}%")

        st.progress(int(confidence))

st.markdown("---")
st.caption("© 2025 NLP Group 25 – Fake News Detection | CCS3356 Natural Language Processing")
