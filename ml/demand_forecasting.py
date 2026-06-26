import pandas as pd

print("=" * 50)
print("DEMAND FORECASTING")
print("=" * 50)

df = pd.read_csv(
    "data/raw/consumption_logs.csv"
)

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns.tolist())


# ==================================
# DAILY DEMAND ANALYSIS
# ==================================

daily_demand = (
    df.groupby("sku_id")["consumed_qty"]
    .mean()
    .reset_index()
)

daily_demand.rename(
    columns={
        "consumed_qty": "avg_daily_demand"
    },
    inplace=True
)

print("\nAVERAGE DAILY DEMAND")
print("-" * 50)

print(
    daily_demand.sort_values(
        by="avg_daily_demand",
        ascending=False
    ).head(10)
)

# ==================================
# 30 DAY DEMAND FORECAST
# ==================================

daily_demand["forecast_30_days"] = (
    daily_demand["avg_daily_demand"] * 30
)

print("\n30 DAY DEMAND FORECAST")
print("-" * 50)

print(
    daily_demand.sort_values(
        by="forecast_30_days",
        ascending=False
    ).head(10)
)


# ==================================
# REORDER ANALYSIS
# ==================================

inventory_df = pd.read_csv(
    "data/raw/inventory_snapshot.csv"
)

reorder_df = daily_demand.merge(
    inventory_df[
        ["sku_id", "current_stock"]
    ],
    on="sku_id",
    how="left"
)

reorder_df["reorder_qty"] = (
    reorder_df["forecast_30_days"]
    -
    reorder_df["current_stock"]
)

reorder_df["reorder_qty"] = (
    reorder_df["reorder_qty"]
    .clip(lower=0)
)

print("\nREORDER RECOMMENDATIONS")
print("-" * 50)

print(
    reorder_df.sort_values(
        by="reorder_qty",
        ascending=False
    ).head(15)
)


# ==================================
# PROCUREMENT PRIORITY
# ==================================

import numpy as np

reorder_df["priority"] = np.where(
    reorder_df["reorder_qty"] > 300,
    "CRITICAL",
    np.where(
        reorder_df["reorder_qty"] > 100,
        "HIGH",
        "NORMAL"
    )
)

print("\nPROCUREMENT PRIORITY")
print("-" * 50)

print(
    reorder_df[
        [
            "sku_id",
            "reorder_qty",
            "priority"
        ]
    ]
    .sort_values(
        by="reorder_qty",
        ascending=False
    )
    .head(20)
)


# ==================================
# PROCUREMENT RECOMMENDATION ENGINE
# ==================================

reorder_df["recommendation"] = np.where(
    reorder_df["priority"] == "CRITICAL",
    "ORDER IMMEDIATELY",
    np.where(
        reorder_df["priority"] == "HIGH",
        "ORDER THIS WEEK",
        "MONITOR"
    )
)

print("\nPROCUREMENT RECOMMENDATIONS")
print("-" * 60)

print(
    reorder_df[
        [
            "sku_id",
            "current_stock",
            "forecast_30_days",
            "reorder_qty",
            "priority",
            "recommendation"
        ]
    ]
    .sort_values(
        by="reorder_qty",
        ascending=False
    )
    .head(20)
)

reorder_df.to_csv(
    "data/processed/procurement_recommendations.csv",
    index=False
)

print("\nPROCUREMENT FILE SAVED")