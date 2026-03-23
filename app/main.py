from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import re
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

class TextInput(BaseModel):
    text: str

def preprocess(text: str):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.get("/")
def home():
    return {"message": "AI Toxic Detector is running"}

@app.post("/predict")
def predict(input: TextInput):
    cleaned = preprocess(input.text)
    vector = vectorizer.transform([cleaned])
    proba = model.predict_proba(vector)[0][1]
    prediction = 1 if proba > 0.65 else 0
    label = "toxic" if prediction == 1 else "non-toxic"

    return {
        "label": label,
        "confidence": float(proba)
    }
