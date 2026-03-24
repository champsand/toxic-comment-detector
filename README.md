# 🧠 Toxic Comment Detection System (v1)

A full-stack AI web application that detects toxic comments using Machine Learning (TF-IDF + Logistic Regression), powered by a FastAPI backend and a lightweight frontend interface.

---

## 🌐 Live Demo

👉 https://toxic-comment-detector-msutiono.vercel.app
🔗 API Endpoint: https://toxic-comment-detector-msutiono.up.railway.app

---

## 🏗️ Architecture

```
Frontend (Vercel) → FastAPI Backend (Railway) → ML Model
```

---

## 🚀 Features

* Detect toxic vs non-toxic comments
* Confidence score for predictions
* Real-time API interaction
* Clean and responsive UI
* Modular and scalable project structure

---

## 🧠 Tech Stack

* **Machine Learning:** Scikit-learn, TF-IDF, Logistic Regression
* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Tools:** Python, Joblib

---

## ⚙️ How It Works

1. User inputs a comment in the frontend
2. Frontend sends a POST request to the FastAPI backend
3. Backend preprocesses the text
4. TF-IDF vectorizer transforms the input
5. Logistic Regression model predicts toxicity
6. Result is returned with a confidence score

---

## 📸 Screenshots

<img width="1919" height="941" alt="image" src="https://github.com/user-attachments/assets/e2570c10-efbb-4026-aff2-2a9ee4e32817" />
<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/172780d9-0451-49d9-9205-28dd84d0ca42" />

---

## 🧪 Run Locally

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

4. Open the frontend:

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
├── app/            # FastAPI backend + trained model
├── training/       # Model training script
├── frontend/       # Frontend UI
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚠️ Notes

* Dataset is not included due to size limitations
* Backend is hosted on Railway (may have cold start delay)
* Model is pre-trained and included for immediate use

---

## 👤 Author

**Matthew Sutiono** - Computer Science Student
