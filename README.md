# 🚀 Toxic Comment Detection System

A full-stack AI application that detects whether a comment is toxic or non-toxic using machine learning.

---

## 🧠 Features

* Text classification using Logistic Regression
* TF-IDF vectorization (1–3 n-grams)
* FastAPI backend for real-time predictions
* Clean frontend with modern UI & animations
* Confidence score output

---

## Dataset

Dataset is not included due to size.
Download it from:
https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset

---

## 🏗️ Tech Stack

* Python (scikit-learn, pandas, numpy)
* FastAPI
* HTML, CSS, JavaScript
* Uvicorn

---

## 📂 Project Structure

```
toxic-comment-detector/
│
├── app/
│   ├── main.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── training/
│   └── train_model.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run Locally

### 1. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run backend

```
python -m uvicorn app.main:app --reload
```

---

### 4. Open frontend

Open:

```
frontend/index.html
```

---

## 🌐 API Endpoint

**POST** `/predict`

### Request:

```
{
  "text": "you are stupid"
}
```

---

### Response:

```
{
  "label": "toxic",
  "confidence": 0.93
}
```

---

## 📊 Model Details

* Model: Logistic Regression
* Vectorizer: TF-IDF (n-grams up to 3)
* Dataset: Toxic comment dataset
* Accuracy: ~0.83–0.87

---

## 🚀 Future Improvements

* Reduce false positives
* Improve dataset quality
* Add deep learning model (BERT)
* Deploy with Docker

---

## 👨‍💻 Author

Built as a portfolio project to demonstrate end-to-end AI system development.
