import sys
import os
import certifi
import pandas as pd
import pymongo

from dotenv import load_dotenv
from fastapi import (
    FastAPI,
    File,
    UploadFile,
    Request,
    Form
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from pydantic import BaseModel

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.constant.training_pipeline import (
    DATA_INGESTION_COLLECTION_NAME,
    DATA_INGESTION_DATABASE_NAME
)

from networksecurity.utils.url_feature_extractor import extract_url_features


# ------------------ ENV SETUP ------------------
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

if not mongo_db_url:
    raise ValueError("MongoDB URL not found in environment variables")

# ------------------ DB CONNECTION ------------------
ca = certifi.where()
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

# ------------------ FASTAPI APP ------------------
app = FastAPI(title="Phishing Detection System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ STATIC & TEMPLATES ------------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ------------------ SCHEMA ------------------
class URLInput(BaseModel):
    url: str


# ------------------ HOME ------------------
@app.get("/")
async def index():
    return RedirectResponse(url="/ui")


# ------------------ UI HOME ------------------
@app.get("/ui", response_class=HTMLResponse)
async def ui_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ------------------ UI URL PREDICTION ------------------
@app.post("/ui/predict-url", response_class=HTMLResponse)
async def ui_predict_url(request: Request, url: str = Form(...)):
    try:
        features = extract_url_features(url)
        df = pd.DataFrame([features])

        preprocessor = load_object("final_models/preprocessor.pkl")
        model = load_object("final_models/model.pkl")
        network_model = NetworkModel(preprocessor, model)

        prediction = network_model.predict(df)[0]

        url_lower = url.lower()
        rule_signals = []

        if any(x in url_lower for x in ["bit.ly", "tinyurl", "goo.gl"]):
            rule_signals.append("Shortened URL")
        if "@" in url_lower:
            rule_signals.append("@ symbol in URL")
        if url_lower.startswith("http://") and any(
            k in url_lower for k in ["login", "verify", "secure", "bank", "account"]
        ):
            rule_signals.append("HTTP + sensitive keywords")

        if prediction == 1:
            result = "🚨 Phishing Website Detected"
        else:
            result = (
                "⚠ Potentially Suspicious (Rule indicators detected)"
                if rule_signals
                else "✅ Legitimate Website"
            )

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": result,
                "rule_signals": rule_signals
            }
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys)


# ------------------ UI CSV PREDICTION ------------------
@app.post("/ui/predict-csv", response_class=HTMLResponse)
async def ui_predict_csv(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        preprocessor = load_object("final_models/preprocessor.pkl")
        model = load_object("final_models/model.pkl")
        network_model = NetworkModel(preprocessor, model)

        predictions = network_model.predict(df)
        df["Prediction"] = [
            "Phishing 🚨" if p == 1 else "Legitimate ✅" for p in predictions
        ]

        table_html = df.to_html(classes="table table-striped", index=False)

        return templates.TemplateResponse(
            "table.html",
            {
                "request": request,
                "table": table_html
            }
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys)


# ------------------ TRAINING API ------------------
@app.get("/train")
async def train_route():
    try:
        pipeline = TrainingPipeline()
        pipeline.run_pipeline()
        return Response("Training completed successfully")
    except Exception as e:
        raise NetworkSecurityException(e, sys)


# ------------------ API CSV PREDICTION ------------------
@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        preprocessor = load_object("final_models/preprocessor.pkl")
        model = load_object("final_models/model.pkl")

        network_model = NetworkModel(preprocessor, model)
        predictions = network_model.predict(df)

        df["predicted_column"] = predictions
        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/output.csv", index=False)

        return {"status": "success", "rows": len(df)}

    except Exception as e:
        raise NetworkSecurityException(e, sys)
