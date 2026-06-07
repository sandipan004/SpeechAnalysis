import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.schemas import Text, Prediction
import pytest
from pydantic import ValidationError

def test_text_schema_preprocessing():
    # Test that text schema preprocessing clean_text is automatically called on validation
    input_text = "Hello! Check out https://google.com."
    text_obj = Text(text=input_text)
    assert text_obj.text == "hello check out url"

def test_prediction_schema_valid():
    pred_data = {
        "toxic": 0.9,
        "severe_toxic": 0.1,
        "obscene": 0.2,
        "threat": 0.0,
        "insult": 0.5,
        "identity_hate": 0.05
    }
    pred = Prediction(**pred_data)
    assert pred.toxic == 0.9
    assert pred.severe_toxic == 0.1

def test_prediction_schema_invalid():
    # If key fields are missing, validation should fail
    pred_data = {
        "toxic": 0.9,
        "severe_toxic": 0.1
    }
    with pytest.raises(ValidationError):
        Prediction(**pred_data)
