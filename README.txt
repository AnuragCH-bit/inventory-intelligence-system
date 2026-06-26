# 📦 Inventory Intelligence System

### AI-Powered Inventory Analytics, Stockout Prediction & Demand Forecasting Platform

An end-to-end Inventory Intelligence System built using **PySpark, Machine Learning, FastAPI, and Power BI** to analyze inventory data, predict stockout risks, forecast future demand, and generate procurement recommendations. The project demonstrates a complete data engineering and machine learning pipeline with an interactive dashboard and production-ready REST API.


# 🚀 Project Overview

Managing inventory efficiently is one of the biggest challenges in supply chain management. Overstocking increases storage costs, while stockouts lead to production delays and lost sales.

This project solves these challenges by combining data engineering, machine learning, business intelligence, and API development into a single platform.

The system performs the following tasks:

* Analyze inventory consumption using PySpark.
* Identify high-risk inventory items.
* Predict stockout risk using Logistic Regression.
* Forecast future demand for each SKU.
* Generate procurement recommendations.
* Visualize business KPIs using Power BI.
* Expose machine learning predictions through a FastAPI REST API with interactive Swagger documentation.


# ✨ Key Features

* 📊 Inventory Analytics using PySpark
* 📦 ABC Inventory Analysis
* ⚠️ Stockout Risk Prediction using Machine Learning
* 📈 Demand Forecasting
* 🛒 Procurement Recommendation Engine
* 📉 Power BI Executive Dashboard
* 🚀 FastAPI REST API
* 📖 Interactive Swagger Documentation
* ✅ Request & Response Validation using Pydantic
* ❤️ Health Check Endpoint
* 🎯 Business Recommendations based on ML Predictions


# 🛠 Technology Stack

 Category             |      Technology          
 -------------------    ------------------- 
 Programming Language    Python              
 Data Processing         PySpark, Pandas     
 Machine Learning        Scikit-learn        
 ML Algorithm            Logistic Regression 
 API Framework           FastAPI             
 Validation              Pydantic            
 API Server              Uvicorn             
 Dashboard               Power BI            
 Version Control         Git & GitHub        
 Model Serialization     Joblib              





## Dataset Design

### Categories
- Bearing
- Seal
- Filter
- Electrical
- Fastener
- Chemical
- Raw Metal
- Consumable

### Embedded Patterns

1. Seasonal Demand
   - Filters increase during Apr-Aug
   - Chemicals increase during Jun-Sep

2. Unreliable Supplier
   - SUP-013
   - High lead time variability
   - Low reliability score

3. Critical Stockout SKUs
   - BRG-0005
   - SEA-0015
   - ELE-0012

### Datasets Generated

- parts_master.csv
- suppliers.csv
- inventory_snapshot.csv
- consumption_logs.csv
- purchase_orders.csv
