from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")

class CustomerFeatures(BaseModel):
    recency_days: float
    frequency_180d: float
    monetary_180d: float
    return_rate_180d: float
    ticket_count_90d: float
    negative_ticket_rate_90d: float
    sessions_30d: float
    product_views_30d: float
    cart_adds_30d: float
    wishlist_adds_30d: float
    abandoned_carts_30d: float
    email_opens_30d: float
    campaign_clicks_30d: float
    last_visit_days_ago: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(customer: CustomerFeatures):

    data = pd.DataFrame([customer.dict()])

    probability = float(
        model.predict_proba(data)[0][1]
    )

    prediction = int(
        model.predict(data)[0]
    )

    if probability > 0.7:
        risk = "high"
    elif probability > 0.4:
        risk = "medium"
    else:
        risk = "low"

    return {
        "churn_probability": round(probability,3),
        "predicted_class": prediction,
        "risk_level": risk,
        "risk_explanation":
        "Higher inactivity and lower engagement increase churn risk."
    }

@app.post("/batch_predict")
def batch_predict(customers: list[CustomerFeatures]):

    data = pd.DataFrame(
        [c.dict() for c in customers]
    )

    probabilities = model.predict_proba(data)[:,1]
    predictions = model.predict(data)

    results = []

    for p, pred in zip(probabilities,predictions):

        results.append({
            "churn_probability": round(float(p),3),
            "predicted_class": int(pred)
        })

    return results