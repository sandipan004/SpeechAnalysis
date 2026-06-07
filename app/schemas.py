import sys
import os
sys.path.append(os.path.abspath(".."))

from pydantic import BaseModel, field_validator
from app.utils import clean_text

class Text(BaseModel):
    text: str
    @field_validator('text')
    @classmethod
    def preprocess(cls, text: str) -> str:
        return clean_text(text)

class Prediction(BaseModel):
    toxic: float
    severe_toxic: float
    obscene: float
    threat: float
    insult: float
    identity_hate: float