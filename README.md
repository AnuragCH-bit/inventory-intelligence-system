# 📦 Enterprise AI Procurement Copilot

An AI-powered Procurement Decision Support System that combines **Machine Learning**, **Business Rules**, **Retrieval-Augmented Generation (RAG)**, and **Large Language Models (LLMs)** to help procurement teams make intelligent inventory replenishment decisions.

---

## 🚀 Overview

Enterprise AI Procurement Copilot is an end-to-end intelligent procurement system that analyzes inventory, predicts stockout risk, retrieves procurement policies, and generates AI-powered recommendations through a REST API and an interactive dashboard.

---

## ✨ Features

### 🤖 AI Procurement Assistant

* AI-powered procurement recommendations
* Natural language question answering
* Context-aware responses using RAG
* Structured JSON output

### 📦 Inventory Intelligence

* Inventory snapshot analysis
* Reorder point evaluation
* Safety stock validation
* Procurement recommendations

### 📈 Machine Learning

* Logistic Regression stockout prediction
* Risk classification
* Confidence estimation
* Feature engineering pipeline

### 📚 Retrieval-Augmented Generation (RAG)

* PDF document ingestion
* Chroma Vector Database
* Semantic search
* HuggingFace Embeddings
* LangChain Retriever

### 📋 Business Rule Engine

* Procurement policy validation
* Inventory evaluation
* Decision support logic

### 🌐 REST API

* FastAPI
* Swagger Documentation
* Pydantic Validation
* JSON APIs

### 💻 User Interface

* Streamlit Dashboard
* AI Recommendation Panel
* Interactive Procurement Queries

---

# 🏗 Complete System Architecture

```text
                              Enterprise AI Procurement Copilot

                                  
                            Synthetic Inventory Data Generation
                                         │
                                         ▼
                             Inventory Datasets (CSV Files)
                                         │
                                         ▼

                            PySpark ETL & Data Processing
                                         │
                                         ▼
                              Data Cleaning & Transformation
                                         │
                                         ▼
                              Feature Engineering Pipeline
                                         │
               ┌─────────────────────────┼─────────────────────────┐
               ▼                         ▼                         ▼
   Weekly Consumption          Days of Supply          Annual Consumption
        Velocity                                           Value
               │                         │                         │
               └─────────────────────────┼─────────────────────────┘
                                         ▼

                              Machine Learning Pipeline
                                         │
                                         ▼
                          Logistic Regression Training Model
                                         │
                                         ▼
                              stockout_model.pkl Generated
                                         │
                                         ▼
                                 FastAPI REST Backend
                                         │
               ┌─────────────────────────┼─────────────────────────┐
               ▼                         ▼                         ▼
           /predict                  /health                  /agent
                                         │
                                         ▼

                                        Day 6
                           Enterprise AI Procurement Agent
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
 Inventory Tool                  ML Prediction Tool               Business Rules
        │                                │                                │
        ▼                                ▼                                ▼
Inventory Snapshot.csv      Logistic Regression             Procurement Logic
        │                                │                                │
        └────────────────────────────────┼────────────────────────────────┘
                                         ▼

                                      
                    Retrieval-Augmented Generation (LangChain)
                                         │
                                         ▼
                             Procurement Policy PDF
                                         │
                                         ▼
                           Recursive Text Chunking
                                         │
                                         ▼
                           HuggingFace Embeddings
                                         │
                                         ▼
                                 Chroma Vector DB
                                         │
                                         ▼
                                   Semantic Search
                                         │
                                         ▼

                                    
                            Prompt Engineering + LLM
                                         │
                                         ▼
                           LangChain Prompt Template
                                         │
                                         ▼
                             Ollama (Llama 3.2 : 3B)
                                         │
                                         ▼
                      Structured AI Procurement Recommendation
                                         │
                                         ▼

                                       
                          Streamlit Dashboard + FastAPI
                                         │
                                         ▼
                               Business User Interface
                                         │
                                         ▼

                             Docker Containerization
                                         │
                                         ▼
      ┌────────────────────────────────────────────────────────────────────┐
      │                         Docker Container                           │
      │                                                                    │
      │  ✓ FastAPI                                                         │
      │  ✓ Streamlit                                                       │
      │  ✓ LangChain                                                       │
      │  ✓ ChromaDB                                                        │
      │  ✓ Scikit-Learn                                                    │
      │  ✓ Pandas                                                          │
      │  ✓ PySpark                                                         │
      │  ✓ Project Source Code                                             │
      │                                                                    │
      └────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
                               Enterprise Deployment
```


---

# 🛠️ Technology Stack

| Category             | Technology         |
| -------------------- | ------------------ |
| Programming Language | Python 3.12        |
| Backend              | FastAPI            |
| Frontend             | Streamlit          |
| Machine Learning     | Scikit-Learn       |
| Data Processing      | Pandas, PySpark    |
| AI Framework         | LangChain          |
| LLM                  | Ollama (Llama 3.2) |
| Embeddings           | HuggingFace MiniLM |
| Vector Database      | ChromaDB           |
| API Validation       | Pydantic           |
| Version Control      | Git & GitHub       |

---






# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/inventory-intelligence-system.git

cd inventory-intelligence-system
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2:3b
```

Start Ollama:

```bash
ollama serve
```

---

# 📚 Build Vector Database

```bash
python rag/ingest.py
```

---

# 🚀 Run FastAPI

```bash
uvicorn api.app:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 💻 Run Streamlit

```bash
streamlit run ui/app.py
```

---



# 🧠 AI Workflow

```text
User Question
      │
      ▼
Inventory Lookup
      │
      ▼
Business Rule Evaluation
      │
      ▼
Machine Learning Prediction
      │
      ▼
Retrieve Procurement Policy
      │
      ▼
Llama 3.2 Analysis
      │
      ▼
Structured Procurement Recommendation
```

---


# 🚀 Future Enhancements

* Docker Support
* Conversation Memory
* Multi-Agent Architecture
* PostgreSQL Integration
* AWS Deployment
* CI/CD Pipeline
* Monitoring & Logging

---

# 👨‍💻 Author

**Anurag Hiwarkar**

AI • Machine Learning • Data Engineering • Generative AI • FastAPI • LangChain • PySpark

GitHub: https://github.com/AnuragCH-bit
