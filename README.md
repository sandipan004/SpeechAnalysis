# SpeechAnalysis
*Developed by Sandipan Dafadar

A machine learning web API and full-stack web application that detects toxic language in user comments using classical ML models (TF-IDF + Logistic Regression). Built with **FastAPI**, trained on the **Jigsaw Toxic Comment Classification Challenge** dataset, and featuring a custom-built premium frontend.

## ✅ Features

- **Beautiful Web Interface**: A modern, glassmorphic dark-mode UI with animated toxicity progress bars.
- Multi-label classification: 
  - `toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`
- Real-time REST API (FastAPI)
- Modular codebase
- Dockerized for instant portability
- Preprocessed with custom regex cleaner


## 🧪 Model Details

- Vectorizer: `TfidfVectorizer` (max_features=4096, stop_words='english')
- Classifier: `LogisticRegression` (class_weight='balanced', max_iter=500, C=1.6)
- Trained on: [Jigsaw Toxic Comment Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## 🗂️ Project Structure

```
SpeechAnalysis/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── model.py
│   ├── schemas.py
│   ├── utils.py
│   └── config.py
├── data/
│   ├── data_processed.csv
│   └── trains.csv
├── models/
│   ├── tf-idf_vectorizer.pkl
│   └── classifier.pkl
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── tf-idf_model_train.ipynb
├── .gitignore
├── docker-requirements.txt
├── Dockerfile
├── README.md
└── requirements.txt
```

## 🧰 Technical Stack
- **Language:** Python 3.12+
- **Framework:** FastAPI (ASGI-compatible)
- **ML Model:**
    - TfidfVectorizer for feature extraction
    - LogisticRegression (one classifier per label, binary relevance method)
- **Serialization:** `dill` for saving sklearn models
- **Request Schema:** Pydantic-based input validation
- **Serving:** Uvicorn for ASGI serving
- **Containerization:** Docker 

## 📡 API Endpoints
The FastAPI server exposes the following endpoints:

### `GET /`

Returns the fully functional Web App interface (HTML/CSS/JS) so users can interact with the toxicity detector directly from their browser.

**Request:**

Open your browser and navigate to:
`http://localhost:8000/`
### `POST /predict`

Performs multi-label classification on the input text and returns the predicted probabilities for each toxicity label.

**Request:**
```
POST /predict
Content-Type: application/json
```
**Request Body:**
```
{
  "text": "You are a criminal person"
}
```
**Response:**
```
{
  "toxic": 0.6774,
  "severe_toxic": 0.039,
  "obscene": 0.0994,
  "threat": 0.1204,
  "insult": 0.5151,
  "identity_hate": 0.6681
}
```

## 🛠️ Git Setup & Repository Cloning
If you haven't installed Git:

### 🔨 Install Git
**Windows:**

Download from https://git-scm.com/download/win and install with default settings.

**Ubuntu/Linux:**
```
sudo apt update
sudo apt install git
```

**macOS:**
```
brew install git
```

### 📦 Clone the Repository
```bash
git clone https://github.com/sandipan004/SpeechAnalysis.git
cd SpeechAnalysis
```

## 🔧 How to Train the Model

Ensure you have the following installed:
- Python (≥ 3.12)
- Conda (for Conda-based setup)
- Virtualenv (install via `pip install virtualenv` if not already available)

### 🐍 Using conda
#### Create a conda virtual environment
Run the following command to create a virtual environment in a specific directory:
```
conda create -p venv python=3.12 -y
```
#### Activate it
```
conda activate venv/
```
#### Install dependencies
```
pip install -r requirements.txt
```

### 💻 Using virtualenv
Run the following command to create a virtual environment in a specific directory:
```
python -m virtualenv venv
```
#### Activate it
- **Windows**
```
venv\Scripts\activate
```
- **Linux/macOS**
```
source venv/bin/activate
```
#### Install dependencies
```
pip install -r requirements.txt
```

Run the provided Python script `train.py` to train the models locally:

```bash
cd notebooks
python train.py
```

This will automatically preprocess the dataset, train the TF-IDF and Logistic Regression models, and save them using `dill` in the `models/` directory.

## 🐳 Docker Setup

🔥 1. Start the Application (Using Docker Compose)
```bash
docker compose up --build -d
```

🚀 2. Stop the Application
```bash
docker compose down
```
You can also access the interactive API docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**Example using cURL**
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "You are a criminal person"}'
```

**Response**
```
{
  "toxic": 0.6774,
  "severe_toxic": 0.039,
  "obscene": 0.0994,
  "threat": 0.1204,
  "insult": 0.5151,
  "identity_hate": 0.6681
}
```
