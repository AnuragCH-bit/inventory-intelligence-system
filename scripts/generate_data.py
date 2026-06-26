import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Categories
categories = {
    "BRG": "Bearing",
    "SEA": "Seal",
    "FIL": "Filter",
    "ELE": "Electrical",
    "FAS": "Fastener",
    "CHE": "Chemical",
    "RAW": "Raw Metal",
    "CON": "Consumable"
}

parts = []

for prefix, category in categories.items():

    for i in range(1, 21):

        sku = f"{prefix}-{i:04d}"

        parts.append({
            "sku_id": sku,
            "part_name": f"{category} Part {i}",
            "category": category,
            "unit_cost": round(np.random.uniform(50, 5000), 2),
            "reorder_point": np.random.randint(100, 500),
            "safety_stock": np.random.randint(50, 200),
            "current_stock": np.random.randint(100, 1000),
            "criticality": np.random.choice(
                ["High", "Medium", "Low"],
                p=[0.2, 0.5, 0.3]
            )
        })

# Create DataFrame
parts_df = pd.DataFrame(parts)

# Save CSV
parts_df.to_csv("data/raw/parts_master.csv", index=False)

print(parts_df.head())
print("\nDataset Shape:", parts_df.shape)
print("\nparts_master.csv saved successfully!")



# -------------------------
# SUPPLIERS DATASET
# -------------------------

suppliers = [
    ("SUP-001", "SKF Industries", "India", 8, 96),
    ("SUP-002", "Timken Global", "USA", 10, 94),
    ("SUP-003", "NSK Components", "Japan", 12, 95),
    ("SUP-004", "Precision Seals Ltd", "Germany", 14, 92),
    ("SUP-005", "FilterTech", "India", 9, 93),
    ("SUP-006", "Electra Systems", "China", 11, 90),
    ("SUP-007", "FastenPro", "India", 7, 97),
    ("SUP-008", "ChemSource", "Singapore", 13, 91),
    ("SUP-009", "MetalWorks", "India", 8, 95),
    ("SUP-010", "Industrial Consumables", "India", 6, 96),
    ("SUP-011", "Prime Bearings", "Germany", 15, 89),
    ("SUP-012", "Advanced Materials", "Japan", 10, 94),

    # Intentionally unreliable supplier
    ("SUP-013", "Global Parts Ltd", "China", 28, 62),

    ("SUP-014", "SupplyChain Corp", "USA", 12, 88),
    ("SUP-015", "Universal Components", "India", 9, 93)
]

suppliers_df = pd.DataFrame(
    suppliers,
    columns=[
        "supplier_id",
        "supplier_name",
        "country",
        "lead_time_days",
        "reliability_score"
    ]
)

suppliers_df.to_csv(
    "data/raw/suppliers.csv",
    index=False
)

print("\nSuppliers Dataset Shape:")
print(suppliers_df.shape)

# -------------------------
# INVENTORY SNAPSHOT
# -------------------------

inventory = []

for _, row in parts_df.iterrows():

    stock = row["current_stock"]

    # Critical stockout SKUs
    if row["sku_id"] in ["BRG-0005", "SEA-0015", "ELE-0012"]:
        stock = np.random.randint(5, 20)

    inventory.append({
        "sku_id": row["sku_id"],
        "current_stock": stock,
        "reorder_point": row["reorder_point"],
        "safety_stock": row["safety_stock"],
        "last_updated": "2026-06-20"
    })

inventory_df = pd.DataFrame(inventory)

inventory_df.to_csv(
    "data/raw/inventory_snapshot.csv",
    index=False
)

print("\nInventory Dataset Shape:")
print(inventory_df.shape)



# -------------------------
# CONSUMPTION LOGS
# -------------------------

from datetime import datetime

plants = [
    "Plant-A",
    "Plant-B",
    "Plant-C",
    "Plant-D"
]

dates = pd.date_range(
    start="2025-01-01",
    end="2026-06-30",
    freq="D"
)

consumption_logs = []

for date in dates:

    for _, part in parts_df.iterrows():

        base_qty = np.random.randint(1, 15)

        # Seasonal Filters
        if (
            part["category"] == "Filter"
            and date.month in [4, 5, 6, 7, 8]
        ):
            base_qty *= 1.4

        # Seasonal Chemicals
        if (
            part["category"] == "Chemical"
            and date.month in [6, 7, 8, 9]
        ):
            base_qty *= 1.3

        # Critical SKUs consume faster
        if part["sku_id"] in [
            "BRG-0005",
            "SEA-0015",
            "ELE-0012"
        ]:
            base_qty *= 2

        consumption_logs.append({
            "date": date,
            "sku_id": part["sku_id"],
            "plant": np.random.choice(plants),
            "consumed_qty": int(base_qty)
        })

consumption_df = pd.DataFrame(
    consumption_logs
)

consumption_df.to_csv(
    "data/raw/consumption_logs.csv",
    index=False
)

print("\nConsumption Dataset Shape:")
print(consumption_df.shape)


# -------------------------
# PURCHASE ORDERS
# -------------------------

purchase_orders = []

for po_num in range(1, 15001):

    supplier = suppliers_df.sample(1).iloc[0]
    part = parts_df.sample(1).iloc[0]

    order_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=np.random.randint(0, 540)
    )

    lead_time = supplier["lead_time_days"]

    # Unreliable supplier behavior
    if supplier["supplier_id"] == "SUP-013":
        lead_time += np.random.randint(5, 20)

    delivery_date = order_date + pd.Timedelta(
        days=int(lead_time)
    )

    purchase_orders.append({
        "po_id": f"PO-{po_num:05d}",
        "sku_id": part["sku_id"],
        "supplier_id": supplier["supplier_id"],
        "order_date": order_date.date(),
        "quantity": np.random.randint(100, 2000),
        "unit_price": round(
            part["unit_cost"] *
            np.random.uniform(0.9, 1.1),
            2
        ),
        "lead_time_days": int(lead_time),
        "delivery_date": delivery_date.date()
    })

po_df = pd.DataFrame(purchase_orders)

po_df.to_csv(
    "data/raw/purchase_orders.csv",
    index=False
)

print("\nPurchase Orders Shape:")
print(po_df.shape)
