from pyspark.sql import SparkSession

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Inventory Intelligence Analytics")
    .getOrCreate()
)

print("=" * 50)
print("SPARK SESSION CREATED SUCCESSFULLY")
print("=" * 50)

# Load Datasets

parts_df = spark.read.csv(
    "data/raw/parts_master.csv",
    header=True,
    inferSchema=True
)

suppliers_df = spark.read.csv(
    "data/raw/suppliers.csv",
    header=True,
    inferSchema=True
)

inventory_df = spark.read.csv(
    "data/raw/inventory_snapshot.csv",
    header=True,
    inferSchema=True
)

consumption_df = spark.read.csv(
    "data/raw/consumption_logs.csv",
    header=True,
    inferSchema=True
)

purchase_orders_df = spark.read.csv(
    "data/raw/purchase_orders.csv",
    header=True,
    inferSchema=True
)

print("\nDATASET COUNTS")
print("-" * 50)

print("Parts Master      :", parts_df.count())
print("Suppliers         :", suppliers_df.count())
print("Inventory         :", inventory_df.count())
print("Consumption Logs  :", consumption_df.count())
print("Purchase Orders   :", purchase_orders_df.count())

# spark.stop()


from pyspark.sql.functions import sum, round

# ----------------------------------
# CONSUMPTION VELOCITY
# ----------------------------------

weeks = 78

velocity_df = (
    consumption_df
    .groupBy("sku_id")
    .agg(
        round(
            sum("consumed_qty") / weeks,
            2
        ).alias("weekly_consumption_velocity")
    )
)

print("\nTOP 10 VELOCITY SKUs")
print("-" * 50)

velocity_df.orderBy(
    velocity_df.weekly_consumption_velocity.desc()
).show(10)

print("VELOCITY CALCULATED")

velocity_df.toPandas().to_csv(
    "data/processed/consumption_velocity.csv",
    index=False
)

print("VELOCITY CSV SAVED")

# Save analytics table

# velocity_df.write.mode("overwrite").csv(
#     "data/processed/consumption_velocity",
#     header=True
# )

# spark.stop()


from pyspark.sql.functions import (
    sum,
    round,
    col,
    avg,
    count,
    when
)

# ----------------------------------
# DAYS OF SUPPLY
# ----------------------------------

daily_consumption_df = (
    consumption_df
    .groupBy("sku_id")
    .agg(
        round(
            sum("consumed_qty") / 546,
            2
        ).alias("daily_consumption")
    )
)

dos_df = (
    inventory_df
    .join(
        daily_consumption_df,
        on="sku_id",
        how="inner"
    )
    .withColumn(
        "days_of_supply",
        round(
            col("current_stock")
            /
            col("daily_consumption"),
            2
        )
    )
)

print("\nLOWEST DAYS OF SUPPLY")
print("-" * 50)

dos_df.select(
    "sku_id",
    "current_stock",
    "daily_consumption",
    "days_of_supply"
).orderBy(
    col("days_of_supply")
).show(10, truncate=False)

print("DOS CALCULATED")

dos_df.toPandas().to_csv(
    "data/processed/days_of_supply.csv",
    index=False
)

print("DOS CSV SAVED")
# dos_df.write.mode("overwrite").csv(
#     "data/processed/days_of_supply",
#     header=True
# )


# ==================================
# PARTS CLASSIFICATION
# ==================================

print("\nSTARTING ABC CLASSIFICATION")
print("-" * 50)

abc_df = (
    consumption_df
    .groupBy("sku_id")
    .agg(
        sum("consumed_qty").alias("total_consumption")
    )
)

abc_df = abc_df.join(
    parts_df.select(
        "sku_id",
        "unit_cost"
    ),
    on="sku_id",
    how="inner"
)

abc_df = abc_df.withColumn(
    "annual_consumption_value",
    col("total_consumption") * col("unit_cost")
)

abc_df.orderBy(
    col("annual_consumption_value").desc()
).show(10, truncate=False)

print("PARTS DATA READY")

# spark.stop()





from pyspark.sql.window import Window
from pyspark.sql.functions import sum as spark_sum, when

# Sort by value descending

window_spec = Window.orderBy(
    col("annual_consumption_value").desc()
)

abc_df = abc_df.withColumn(
    "cumulative_value",
    spark_sum(
        "annual_consumption_value"
    ).over(window_spec)
)

total_value = abc_df.agg(
    spark_sum(
        "annual_consumption_value"
    )
).collect()[0][0]

abc_df = abc_df.withColumn(
    "cumulative_percent",
    (col("cumulative_value") / total_value) * 100
)

abc_df = abc_df.withColumn(
    "abc_category",
    when(
        col("cumulative_percent") <= 70,
        "A"
    )
    .when(
        col("cumulative_percent") <= 90,
        "B"
    )
    .otherwise("C")
)

print("\nABC CLASSIFICATION")
print("-" * 50)

abc_df.select(
    "sku_id",
    "annual_consumption_value",
    "abc_category"
).show(20, truncate=False)





# ==================================
# SUPPLIER RELIABILITY ANALYTICS
# ==================================

print("\nSUPPLIER RELIABILITY ANALYTICS")
print("-" * 50)

supplier_metrics_df = (
    purchase_orders_df
    .groupBy("supplier_id")
    .agg(
        round(
            avg("lead_time_days"),
            2
        ).alias("avg_lead_time"),
        count("*").alias("total_orders")
    )
)

supplier_metrics_df = (
    supplier_metrics_df
    .join(
        suppliers_df.select(
            "supplier_id",
            "supplier_name",
            "reliability_score"
        ),
        on="supplier_id",
        how="inner"
    )
)

supplier_metrics_df.orderBy(
    col("avg_lead_time").desc()
).show(
    truncate=False
)

print("SUPPLIER ANALYTICS READY")






# ==================================
# INVENTORY RISK SCORE
# ==================================

print("\nINVENTORY RISK ANALYSIS")
print("-" * 50)

risk_df = (
    velocity_df
    .join(
        dos_df.select(
            "sku_id",
            "days_of_supply"
        ),
        on="sku_id",
        how="inner"
    )
)

risk_df = risk_df.withColumn(
    "risk_level",
    when(
        col("days_of_supply") < 5,
        "HIGH"
    )
    .when(
        col("days_of_supply") < 15,
        "MEDIUM"
    )
    .otherwise("LOW")
)

risk_df.select(
    "sku_id",
    "weekly_consumption_velocity",
    "days_of_supply",
    "risk_level"
).orderBy(
    col("days_of_supply")
).show(20, truncate=False)



spark.stop()