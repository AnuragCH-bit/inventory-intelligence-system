from fastapi import FastAPI, HTTPException
from api.schemas import (
    StockPredictionRequest,
    StockPredictionResponse
)
import pandas as pd
import joblib

app = FastAPI(

    title="Inventory Intelligence Prediction API",

    description="""
    Machine Learning API for predicting inventory stockout risk.

    Features:
    • Stockout Prediction
    • Confidence Score
    • Business Recommendation
    • Health Check Endpoint
    """,

    version="1.0.0",

    contact={
        "name": "Anurag Hiwarkar",
        "email": "anurag@example.com"
    },

    license_info={
        "name": "MIT License"
    }

)

# Load ML Model 
model = joblib.load(
    "ml/stockout_model.pkl"
)

print("=" * 50)
print("MODEL LOADED SUCCESSFULLY")
print(model)
print("=" * 50)


@app.get(

    "/",

    tags=["Home"],

    summary="Application Home",

    description="Returns a welcome message."

)

def home():
    return {
        "message": "Inventory Intelligence API Running Successfully"
    }


@app.post(

    "/predict",

    response_model=StockPredictionResponse,

    tags=["Prediction"],

    summary="Predict Inventory Stockout Risk",

    description="""
Predicts whether an inventory item is at risk of stockout
using the trained Logistic Regression model.
"""

)
def predict(data: StockPredictionRequest):

    try:

        features = pd.DataFrame(
            [[
                data.weekly_consumption_velocity,
                data.days_of_supply,
                data.annual_consumption_value,
                data.current_stock
            ]],
            columns=[
                "weekly_consumption_velocity",
                "days_of_supply",
                "annual_consumption_value",
                "current_stock"
            ]
        )

        prediction = model.predict(features)

        probability = model.predict_proba(features)

        confidence = round(
            probability[0][prediction[0]] * 100,
            2
        )

        if prediction[0] == 1:

            risk = "HIGH STOCKOUT RISK"

            recommendation = (
                "Immediate replenishment required. "
                "Raise purchase order."
            )

        else:

            risk = "LOW STOCKOUT RISK"

            recommendation = (
                "Inventory level is healthy. "
                "Continue regular monitoring."
            )

        return {

            "prediction": int(prediction[0]),

            "risk": risk,

            "confidence": confidence,

            "recommendation": recommendation

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
    

@app.get(

    "/health",

    tags=["Health"],

    summary="Health Check",

    description="Checks whether the API and ML model are running."

)

def health():

    return {

        "status": "Healthy",

        "api": "Running",

        "model": "Loaded",

        "version": "1.0.0"

    }