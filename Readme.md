# AI-Powered Cloud Stock Analytics: Global Tech Pipeline 📈☁️🤖

An end-to-end cloud-based data engineering and AI analytics pipeline designed to automate the ingestion, transformation, analysis, and visualization of global technology stock market data.

This project integrates Microsoft Azure cloud services, Apache Spark, and Generative AI to build a scalable analytics platform capable of generating technical indicators, AI-driven market insights, and interactive dashboards.

## 📖 Project Overview

This system collects stock market data and processes it through a multi-layer cloud data architecture. Using Generative AI, the system converts numerical indicators into human-readable market signals, which are then visualized through an interactive Power BI dashboard for easier decision-making.

## 📁 Project Structure

### ⚡ `Stock_ETL.ipynb`

The primary Azure Databricks notebook implementing the Medallion Architecture (Bronze, Silver, Gold).

- Data Cleaning: Preprocessing using PySpark and schema validation.
- Time-Series Analysis: Using Spark Window Functions to calculate SMA50 and SMA200.

### 📥 `ingest_stocks.py`

A standalone Python script for data collection.

- API Integration: Fetches data via the Yahoo Finance API.
- Cloud Storage: Automatically uploads raw CSV files to Azure Data Lake Storage (ADLS Gen2).

### 📊 `CBDA.pbix`

The Power BI dashboard file that connects to the Gold layer.

- Provides interactive visualizations for price trends, volume, and AI-generated sentiment cards.

### 📄 `CBDAS_projectReport.pdf`

The complete technical documentation covering methodology, hardware/software requirements, and final implementation results.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Cloud Platform | Microsoft Azure |
| Cloud Storage | Azure Data Lake Storage Gen2 |
| Data Processing | Apache Spark (PySpark) |
| Engineering Platform | Azure Databricks |
| Generative AI | Gemini 2.5 Flash API |
| Data Visualization | Power BI Desktop |
| Language | Python 3.x |

## 🚀 Core Features

### 1. 🥉🥈🥇 Three-Tier Medallion Architecture

The pipeline ensures data quality and traceability through three distinct layers:

- Bronze (Raw): Immutable source of truth ingested directly from the API.
- Silver (Cleaned): Standardized data with validated schemas and removed nulls.
- Gold (Analytics): Curated tables with computed SMA50, SMA200, and AI insights.

### 2. 🤖 AI-Driven Market Sentiment

The system integrates the Gemini 2.5 Flash API to transform traditional technical analysis into AI-assisted financial guidance.

It interprets SMA crossovers to flag:

- Bullish signals for potential upward trends.
- Bearish signals for potential downward trends.

### 3. 📊 Interactive Data Visualization

The Power BI dashboard allows users to filter by tickers like NVDA, AAPL, and MSFT, observe crossover events, and view automated portfolio recommendations.

## ⚙️ Running the Project

### Step 1: 📥 Data Ingestion

Run the ingestion script locally or in a cloud VM:

```bash
python ingest_stocks.py
```

### Step 2: ⚡ ETL and AI Integration

1. Import `Stock_ETL.ipynb` into Azure Databricks.
2. Configure your Azure Storage Key and Gemini API Key in the setup cells.
3. Execute the notebook to process data from Bronze to Gold.

### Step 3: 📊 Visualization

1. Open `CBDA.pbix` in Power BI Desktop.
2. Update the data source to point to your Azure Gold layer.
3. Refresh the dataset to see the live dashboard.

## 🎓 Learning Outcomes and Future Enhancements

This project demonstrates proficiency in Cloud Computing, Big Data Processing, and AI Integration.

Future roadmap:

- Implement real-time streaming with Azure Event Hub.
- Add advanced indicators like RSI and MACD.
- Deploy the AI model as a microservice using Azure Machine Learning.
