import pandas as pd
from pathlib import Path

DATA_PATH = Path("data") / "raw"

INVENTORY_FILE = DATA_PATH / "inventory_snapshot.csv"




# Load Inventory Data Once
# (Loaded when application starts)
inventory_df = pd.read_csv(
    INVENTORY_FILE
)


# Inventory Tool
def get_inventory_details(sku: str):

    filtered_data = inventory_df[
    inventory_df["sku_id"] == sku
]

    if filtered_data.empty:

        return None
    return filtered_data.iloc[0].to_dict()


