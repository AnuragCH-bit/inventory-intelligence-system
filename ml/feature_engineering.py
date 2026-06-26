from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Feature Engineering")
    .getOrCreate()
)

print("FEATURE ENGINEERING STARTED")


# ==================================
# LOAD ANALYTICS DATASETS
# ==================================

velocity_df = spark.read.csv(
    "data/processed/consumption_velocity.csv",
    header=True,
    inferSchema=True
)

dos_df = spark.read.csv(
    "data/processed/days_of_supply.csv",
    header=True,
    inferSchema=True
)

abc_df = spark.read.csv(
    "data/processed/abc_classification.csv",
    header=True,
    inferSchema=True
)

supplier_df = spark.read.csv(
    "data/processed/supplier_metrics.csv",
    header=True,
    inferSchema=True
)

risk_df = spark.read.csv(
    "data/processed/inventory_risk.csv",
    header=True,
    inferSchema=True
)

print("\nANALYTICS DATA LOADED")
print("-" * 50)

print("Velocity Rows :", velocity_df.count())
print("DOS Rows      :", dos_df.count())
print("ABC Rows      :", abc_df.count())
print("Risk Rows     :", risk_df.count())
print("Supplier Rows :", supplier_df.count())




from pyspark.sql.functions import when, col

# ==================================
# CREATE MASTER FEATURE DATASET
# ==================================

inventory_df = spark.read.csv(
    "data/raw/inventory_snapshot.csv",
    header=True,
    inferSchema=True
)

feature_df = (
    velocity_df
    .join(
        dos_df.select(
            "sku_id",
            "days_of_supply"
        ),
        on="sku_id",
        how="inner"
    )
    .join(
        abc_df.select(
            "sku_id",
            "annual_consumption_value"
        ),
        on="sku_id",
        how="inner"
    )
    .join(
        risk_df.select(
            "sku_id",
            "risk_level"
        ),
        on="sku_id",
        how="inner"
    )
    .join(
        inventory_df.select(
            "sku_id",
            "current_stock"
        ),
        on="sku_id",
        how="inner"
    )
)

print("\nMASTER FEATURE DATASET")
print("-" * 50)

feature_df.show(10, truncate=False)

print("FEATURE DATASET CREATED")




# ==================================
# CREATE TARGET VARIABLE
# ==================================

feature_df = feature_df.withColumn(
    "stockout_target",
    when(
        col("days_of_supply") < 5,
        1
    ).otherwise(0)
)

print("\nSTOCKOUT TARGET CREATED")
print("-" * 50)

feature_df.select(
    "sku_id",
    "days_of_supply",
    "stockout_target"
).orderBy(
    col("days_of_supply")
).show(20, truncate=False)



print("\nSAVING ML TRAINING DATASET")
print("-" * 50)

feature_df.toPandas().to_csv(
    "data/processed/ml_training_dataset.csv",
    index=False
)

print("ML TRAINING DATASET SAVED")


spark.stop()