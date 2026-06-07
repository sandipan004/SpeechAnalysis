import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello and welcome to SpeechFlowGuard API"}

def test_predict_endpoint_clean_input():
    payload = {"text": "You are a wonderful friend"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    # Ensure all labels are present
    labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    for label in labels:
        assert label in data
        assert isinstance(data[label], float)
        assert 0.0 <= data[label] <= 1.0

def test_predict_endpoint_toxic_input():
    payload = {"text": "You are stupid and I hate you"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    # Toxic probability should be relatively high
    assert data["toxic"] > 0.5
    assert data["insult"] > 0.3

def test_predict_endpoint_empty_input():
    # If the text is empty or cleaned to be empty
    payload = {"text": "   "}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "toxic" in data
