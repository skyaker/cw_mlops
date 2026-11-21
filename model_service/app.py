from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

MODEL = joblib.load("bank_marketing_logreg.joblib")

app = FastAPI(title="Bank Marketing Model")


class Customer(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: Literal["yes", "no"]
    balance: int
    housing: Literal["yes", "no"]
    loan: Literal["yes", "no"]
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer) -> dict:
    data = pd.DataFrame([customer.model_dump()])
    prediction = int(MODEL.predict(data)[0])
    probability = float(MODEL.predict_proba(data)[0, 1])
    return {
        "prediction": "yes" if prediction else "no",
        "probability_yes": round(probability, 4),
    }
