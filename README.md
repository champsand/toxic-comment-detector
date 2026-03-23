# Toxic Comment Detection System

A full-stack AI application that detects toxic comments using Machine Learning (TF-IDF + Logistic Regression) with a FastAPI backend and simple frontend interface.

---

## 🚀 Features

* Detect toxic vs non-toxic comments
* Confidence score for predictions
* FastAPI backend API
* Lightweight frontend interface
* Clean modular project structure

---

## 🧠 Tech Stack

* **Machine Learning:** Scikit-learn, TF-IDF, Logistic Regression
* **Backend:** FastAPI
* **Frontend:** HTML, JavaScript
* **Tools:** Python, Joblib

---

## 📸 Screenshots

COMING SOON

---

## 🎥 Demo

COMING SOON

---

## ⚙️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/champsand/toxic-comment-detector.git
cd toxic-comment-detector
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend:

```bash
uvicorn app.main:app --reload
```

4. Open frontend:

* Open `frontend/index.html` in your browser

---

## 📡 API Endpoint

### POST `/predict`

Request:

```json
{
  "text": "your comment here"
}
```

Response:

```json
{
  "prediction": "toxic",
  "confidence": 0.87
}
```

---

## 📁 Project Structure

```
toxic-comment-detector/
│
├── app/            # FastAPI backend + model
├── training/       # Model training script
├── frontend/       # UI
├── requirements.txt
├── README.md
```

---

## ⚠️ Notes

* Dataset is not included due to size limitations
* Model is pre-trained and included for immediate use

---

## 👤 Author

Matthew Sutiono — Computer Science Student
