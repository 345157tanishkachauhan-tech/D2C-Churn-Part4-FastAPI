from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

def test_predict():

    payload = {
        "recency_days":10,
        "frequency_180d":5,
        "monetary_180d":5000,
        "return_rate_180d":0.1,
        "ticket_count_90d":1,
        "negative_ticket_rate_90d":0.1,
        "sessions_30d":20,
        "product_views_30d":30,
        "cart_adds_30d":5,
        "wishlist_adds_30d":3,
        "abandoned_carts_30d":1,
        "email_opens_30d":5,
        "campaign_clicks_30d":2,
        "last_visit_days_ago":2
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

def test_batch_predict():

    payload = [
        {
            "recency_days":10,
            "frequency_180d":5,
            "monetary_180d":5000,
            "return_rate_180d":0.1,
            "ticket_count_90d":1,
            "negative_ticket_rate_90d":0.1,
            "sessions_30d":20,
            "product_views_30d":30,
            "cart_adds_30d":5,
            "wishlist_adds_30d":3,
            "abandoned_carts_30d":1,
            "email_opens_30d":5,
            "campaign_clicks_30d":2,
            "last_visit_days_ago":2
        }
    ]

    response = client.post(
        "/batch_predict",
        json=payload
    )

    assert response.status_code == 200