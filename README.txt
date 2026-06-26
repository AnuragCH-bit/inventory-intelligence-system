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


# 🏗 System Architecture


                        Inventory Intelligence System

                           Synthetic Data Generation
                                      │
                                      ▼
                            Inventory Datasets (CSV)
                                      │
                                      ▼
                           PySpark Data Processing
                                      │
                                      ▼
                       Feature Engineering & Analytics
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
 Stockout Prediction          Demand Forecasting      Procurement Recommendation
(Logistic Regression)         (30-Day Forecast)        (Reorder Quantity)
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      ▼
                             Power BI Dashboard
                                      │
                                      ▼
                             FastAPI REST API
                                      │
                                      ▼
                         Business Users / Managers



# 🔄 Project Workflow

1. Generate synthetic inventory datasets.
2. Perform large-scale analytics using PySpark.
3. Engineer features for machine learning.
4. Train a Logistic Regression model to predict stockout risk.
5. Forecast future demand for each SKU.
6. Generate procurement recommendations.
7. Visualize KPIs using Power BI.
8. Deploy the trained ML model using FastAPI.
9. Serve real-time predictions through REST APIs.




# 📁 Project Structure
inventory-intelligence-system/
│
├── api/
│   ├── app.py
│   └── schemas.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── Inventory_Intelligence.pbix
│
├── ml/
│   ├── stockout_model.py
│   ├── demand_forecasting.py
│   ├── feature_engineering.py
│   └── stockout_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore




# ⚙️ Installation Guide

## 1. Clone the Repository

bash
git clone https://github.com/AnuragCH-bit/inventory-intelligence-system.git


## 2. Navigate to the Project

bash
cd inventory-intelligence-system


## 3. Create Virtual Environment

### Windows

bash
python -m venv .venv
Activate Virtual Environment

bash
.venv\Scripts\activate


### Linux / macOS

bash
python3 -m venv .venv
source .venv/bin/activate


## 4. Install Dependencies

bash
pip install -r requirements.txt


# ▶️ How to Run the Project

### Step 1

Run the Machine Learning pipeline.

bash
python ml/feature_engineering.py

python ml/stockout_model.py

python ml/demand_forecasting.py


### Step 2

Start FastAPI Server

bash
uvicorn api.app:app --reload


### Step 3

Open Swagger Documentation

text
http://127.0.0.1:8000/docs


### Step 4

Test Prediction API

Use the `/predict` endpoint in Swagger UI and provide the required inventory values to receive:

* Stockout Prediction
* Confidence Score
* Business Recommendation



# 🌐 API Endpoints

| Method | Endpoint   | Description           |
| ------ | ---------- | --------------------- |
| GET    | `/`        | Home Endpoint         |
| GET    | `/health`  | Health Check Endpoint |
| POST   | `/predict` | Predict Stockout Risk |



`json
{
  "prediction": 0,
  "risk": "LOW STOCKOUT RISK",
  "confidence": 97.06,
  "recommendation": "Inventory level is healthy. Continue regular monitoring."
}



# 🤖 Machine Learning Pipeline

The project uses a Logistic Regression model to predict stockout risk.

### Features Used

* Weekly Consumption Velocity
* Days of Supply
* Annual Consumption Value
* Current Stock

### Target

* Stockout Risk (0 = Low Risk, 1 = High Risk)

### Model Performance

* Algorithm: Logistic Regression
* Class Balancing: Enabled
* Model Serialization: Joblib
* Prediction Confidence: Implemented using `predict_proba()`



# 📊 Power BI Dashboard

### Dashboard Includes

* Executive KPI Summary
* Total SKUs
* High Risk SKUs
* Critical Procurement Items
* Supplier Analysis
* Risk Distribution
* Top Risk Inventory
* Procurement Recommendations



## Live Demo

### API URL

https://inventory-intelligence-system.onrender.com

### Swagger Documentation

https://inventory-intelligence-system.onrender.com/docs

### Health check

https://inventory-intelligence-system.onrender.com/health




# 📈 Project Results

The Inventory Intelligence System successfully demonstrates an end-to-end data engineering and machine learning pipeline for inventory optimization.

### Key Outcomes

This project demonstrates the complete lifecycle of a production-ready inventory analytics solution.

* Generated realistic synthetic inventory datasets.
* Performed large-scale analytics using PySpark.
* Built a Logistic Regression model for stockout prediction.
* Generated demand forecasts and procurement recommendations.
* Designed an interactive Power BI dashboard for business users.
* Deployed the trained machine learning model as a REST API using FastAPI.
* Implemented request validation, response validation, confidence scores, and health monitoring.




# 🚀 Future Enhancements

The following enhancements can be implemented in future versions of the project:

* Deploy the API on AWS EC2 or Azure.
* Containerize the application using Docker.
* Build CI/CD pipelines using GitHub Actions.
* Replace batch processing with real-time streaming using Apache Kafka.
* Integrate with ERP systems such as SAP or Oracle.
* Add advanced forecasting models such as XGBoost or LSTM.
* Implement authentication and authorization for API security.
* Store predictions in PostgreSQL for historical analysis.


# 💡 Skills Demonstrated

This project demonstrates practical experience in:

* Python Programming
* Data Engineering
* PySpark
* Feature Engineering
* Machine Learning
* Logistic Regression
* FastAPI Development
* REST API Design
* Pydantic Validation
* Power BI Dashboard Development
* Git & GitHub
* Model Deployment
* Business Analytics



# 👨‍💻 Author

**Anurag Hiwarkar**

Aspiring Data Engineer | Machine Learning Enthusiast | Python Developer

### Connect With Me

* GitHub: https://github.com/AnuragCH-bit




# 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project for educational and learning purposes.


