import sys
import os
sys.path.append(os.path.abspath(".."))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import router

app = FastAPI(title="SpeechAnalyis")

# Mount static directory for frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
