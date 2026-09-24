from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# --------------------------------------------------
# Load model
# --------------------------------------------------

MODEL_PATH = "random_forest_balanced_model.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="EV Adoption Prediction API",
    description="API for EV adoption prediction",
    version="1.0.0"
)


# --------------------------------------------------
# Features
# --------------------------------------------------

FEATURES = [
    "Age",
    "Annual_Income_USD",
    "Daily_Commute_km",
    "Number_of_Cars_Owned",
    "Charging_Stations_Near_Home",
    "Charging_Stations_Near_Work",
    "Environmental_Concern_Level",

    "Gender_Male",
    "Gender_Other",

    "City_Type_Suburban",
    "City_Type_Urban",

    "Current_Car_Type_SUV",
    "Current_Car_Type_Sedan",
    "Current_Car_Type_Truck",

    "Home_Charging_Possible_Yes",
    "Subsidy_Available_Yes",

    # Range Anxiety
    "Range_Anxiety_Level_Low",
    "Range_Anxiety_Level_Medium"
]


# --------------------------------------------------
# Request schema
# --------------------------------------------------

class PredictionRequest(BaseModel):
    Age: float
    Annual_Income_USD: float
    Daily_Commute_km: float
    Number_of_Cars_Owned: float

    Charging_Stations_Near_Home: float
    Charging_Stations_Near_Work: float
    Environmental_Concern_Level: float

    Gender_Male: int
    Gender_Other: int

    City_Type_Suburban: int
    City_Type_Urban: int

    Current_Car_Type_SUV: int
    Current_Car_Type_Sedan: int
    Current_Car_Type_Truck: int

    Home_Charging_Possible_Yes: int
    Subsidy_Available_Yes: int

    Range_Anxiety_Level_Low: int
    Range_Anxiety_Level_Medium: int


# --------------------------------------------------
# Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "EV Adoption Prediction API is running"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(request: PredictionRequest):

    data = request.model_dump()

    input_data = pd.DataFrame([data])
    input_data = input_data[FEATURES]

    prediction = model.predict(input_data)[0]

    # Convert numpy types to native Python types
    if hasattr(prediction, "item"):
        prediction = prediction.item()

    response = {
        "prediction": prediction
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]

        response["probability"] = float(max(probabilities))

    return response

