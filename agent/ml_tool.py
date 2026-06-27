from pathlib import Path
import joblib

MODEL_PATH = Path("ml") / "stockout_model.pkl"

MODEL = joblib.load(MODEL_PATH)

def predict_stockout(
    features: list
):

    prediction = MODEL.predict(
        [features]
    )

    return prediction[0]