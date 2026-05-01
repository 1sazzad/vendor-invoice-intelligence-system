# Vendor Invoice Intelligence System

An end-to-end Machine Learning project that predicts freight costs and detects suspicious vendor invoices to reduce financial leakage and manual auditing effort.

---

## Business Problem

Companies receive thousands of vendor invoices regularly.

Finance teams manually verify whether:

- Freight charges are reasonable
- Vendors are overcharging
- Invoice values are suspicious
- Manual auditing workload is too high

### Real-world issue:
An accounts executive manually reviews invoices daily, which causes:

- Human error
- Slow processing
- Financial leakage
- Fraud risks
- Operational inefficiency

---

## Solution

This system automates invoice verification by:

1. Predicting expected freight cost
2. Comparing actual freight cost vs predicted freight cost
3. Flagging suspicious invoices

---

## Features

- Freight Cost Prediction
- Overcharged Invoice Detection
- Undercharged Invoice Detection
- Real-time invoice analysis
- Streamlit dashboard
- SQL data extraction
- Model comparison

---

# Project Workflow

```text
SQLite Database
→ SQL Data Extraction
→ Data Cleaning
→ Feature Engineering
→ Exploratory Data Analysis
→ Model Training
→ Model Evaluation
→ Model Saving
→ Streamlit Deployment
```

---

# Dataset Information

Database Size: **404 MB**

Tables:

| Table Name | Rows |
|------------|--------|
| purchases | 2,372,474 |
| purchase_prices | 12,261 |
| vendor_invoice | 5,543 |
| begin_inventory | 206,529 |
| end_inventory | 224,489 |

---

# Tech Stack

### Backend/Data Processing
- Python
- SQLite
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Deployment
- Streamlit

### Version Control
- Git
- GitHub

---

# Project Structure

```text
vendor-invoice-intelligence/
│
├── data/
│   ├── inventory.db
│   └── processed_invoice_data.csv
│
├── models/
│   ├── best_freight_model.pkl
│   └── feature_columns.pkl
│
├── src/
│   ├── extract_data.py
│   ├── preprocess.py
│   ├── train_models.py
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Data Extraction

Data was extracted from SQLite database using SQL joins:

- purchases
- purchase_prices
- vendor_invoice

Aggregated metrics:

- Total Quantity
- Total Purchase Dollars
- Average Purchase Price
- Freight Cost

---

# Feature Engineering

Created additional features:

- Freight Per Unit
- Purchase Cost Per Unit

Created risk detection logic:

- Overcharged Invoice
- Undercharged Invoice
- Normal Invoice

---

# Models Used

## 1. Linear Regression
Used for baseline freight prediction

### Training Time:
~2–20 seconds

---

## 2. Decision Tree Regressor
Used for non-linear relationships

### Training Time:
~10 seconds–2 minutes

---

## 3. Random Forest Regressor
Used for ensemble learning

### Training Time:
~2–10 minutes

---

# Evaluation Metrics

- MAE
- RMSE
- R² Score

---

# Business Logic for Invoice Detection

### Overcharged Invoice

```python
actual > predicted * 1.3
```

---

### Undercharged / Suspicious Invoice

```python
actual < predicted * 0.7
```

---

### Normal Invoice

```python
0.7 <= actual/predicted <= 1.3
```

---

# Deployment

Built using Streamlit.

Run locally:

```bash
streamlit run app.py
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/yourusername/vendor-invoice-intelligence.git
```

Move into folder:

```bash
cd vendor-invoice-intelligence
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

### Step 1: Extract Data

```bash
python src/extract_data.py
```

### Step 2: Train Models

```bash
python src/train_models.py
```

### Step 3: Run Streamlit App

```bash
streamlit run app.py
```

---

# Future Improvements

- FastAPI deployment
- Docker containerization
- Airflow pipeline automation
- PostgreSQL integration
- MLflow model tracking
- Cloud deployment (AWS/GCP/Azure)

---

# Project Outcome

This project reduces:

- Manual invoice review effort
- Financial leakage
- Fraud risk

And improves:

- Automation
- Operational efficiency
- Decision-making speed

---

# Author

MD Sazzad Hossain

- CSE Student, Institute of Science and Technology (IST)
- President, Programming Club of IST (pcIST)
- Aspiring Data Engineer / ML Engineer
