import pandas as pd
from pathlib import Path

DATA_PATH = Path("data") / "processed"

ML_FILE = DATA_PATH / "ml_training_dataset.csv"

ml_df = pd.read_csv(ML_FILE)


def get_ml_features(sku: str):

    row = ml_df[
        ml_df["sku_id"] == sku
    ]

    if row.empty:
        return None

    row = row.iloc[0]

    return {
        "weekly_consumption_velocity": row["weekly_consumption_velocity"],
        "days_of_supply": row["days_of_supply"],
        "annual_consumption_value": row["annual_consumption_value"],
        "current_stock": row["current_stock"]
    }