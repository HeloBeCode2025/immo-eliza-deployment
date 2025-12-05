# 🏡 Immo-Eliza — Full Deployment Project  
*A complete ML → API → Web App pipeline for real-estate price prediction*

This project contains the **end-to-end workflow** for deploying a machine-learning model that predicts Belgian real-estate prices. It integrates:

1. **Data cleaning & preprocessing**  
2. **Model training**  
3. **API deployment** (FastAPI + Docker, hosted on Northflank)  
4. **Web application UI** (Streamlit Cloud)  
5. A fully automated pipeline for real-world estimation  

---

## 📁 Repository Structure (Main Project)

IMMO-ELIZA-DEPLOYMENT/
```
├── best_price_model.joblib
├── clean_data.csv
├── data_preprocessing.py
├── Dockerfile
├── model_features.joblib
├── my_api.py # API code for FastAPI (development version)
├── price_scaler.joblib
├── README.md # ← you are here
├── requirements.txt
└── UI.py # Streamlit UI (development version)
```

This repository is the **canonical source** for:

- the training pipeline  
- the preprocessing logic  
- the inference artifacts (model + scaler + feature list)  
- documentation about the full ML → API → UI workflow  

Two additional repositories depend on it.

---

# 🚀 Project Components

## 1️⃣ Machine Learning Model (This Repository)

This is where the core model is built:

- Load & clean the real-estate dataset  
- Encode categorical features + enrich with postal/province/region  
- Normalize the target (`price`)  
- Train multiple regression models 
- Export:

best_price_model.joblib

model_features.joblib 

price_scaler.joblib


This ensures that both the API and UI use the **same preprocessing and feature space**.

---

## 2️⃣ Prediction API (FastAPI + Docker + Northflank)

📂 **Repository:** `IMMO-ELIZA-DEPLOYMENT-API`  
🌐 **Live URL:**  
https://p01--immo-eliza-api--j9cqmtc6d89m.code.run


This repository contains:
```
IMMO-ELIZA-DEPLOYMENT-API/
├── best_price_model.joblib
├── clean_data.csv
├── data_preprocessing.py
├── Dockerfile
├── model_features.joblib
├── my_api.py # FastAPI application
├── price_scaler.joblib
└── requirements.txt
```

The API exposes a `/predict` endpoint that:

1. Accepts a JSON payload describing a property  
2. Applies preprocessing  
3. Runs the ML model  
4. Inverse-transforms the predicted price  
5. Returns the estimate to the UI  

This API is deployed on **Northflank** and runs inside a Docker container.

---

## 3️⃣ Web User Interface (Streamlit Web App)

📂 **Repository:** `IMMO-ELIZA-DEPLOYMENT-UI`  
🌐 **Streamlit URL:**  
https://immo-eliza-ui.streamlit.app


This repository contains:
```
IMMO-ELIZA-DEPLOYMENT-UI/
├── best_price_model.joblib
├── clean_data.csv
├── data_preprocessing.py
├── model_features.joblib
├── price_scaler.joblib
├── requirements.txt
└── UI.py # full multi-step interface
```

The UI allows users to:

- enter property information step-by-step  
- dynamically update subtypes based on category  
- validate postal codes  
- call the backend API  
- display the final predicted price  

---

# 🔗 How Everything Fits Together
```
[ Training Repo ]
↓ exports
best_price_model.joblib
model_features.joblib
price_scaler.joblib
↓ copied into
──────────────────────────────────
[ API Repo (Northflank) ]
|
| JSON request
↓
/predict endpoint
|
↓ JSON response
──────────────────────────────────
[ UI Repo (Streamlit Cloud) ]
```

The **training repo** is where the models get trained and compared.  
The **API repo** uses the trained artifacts to expose predictions.  
The **UI repo** calls the API and presents results to the user.

---

# 🛠 Local Development

### 1. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the API locally

uvicorn my_api:app --reload

### 3. Run the Streamlit UI locally

streamlit run UI.py

