# Data-Driven Investment Intelligence Using NIFTY-50 Market Data

## Motivation
This repository contains the source code for an AI-powered investment intelligence platform developed for the NIFTY 50 Cult Open Projects 2026. The platform transforms 21 years of raw historical NSE data into practical decision-support systems.

## Deliverables Included
1. **Stock Predictor Engine:** A Random Forest Classifier predicting daily directional movement utilizing engineered features (RSI, MACD, SMA).
2. **Portfolio Construction Module:** Modern Portfolio Theory (MPT) implementation generating Conservative, Balanced, and Aggressive allocations based on historical risk profiles.
3. **Risk Assessment Module:** Quantitative analytics calculating Sharpe Ratio, Sortino Ratio, and Maximum Drawdowns across multiple market crashes.

## Environment Setup & Reproducing Results
1. Clone this repository to your local machine.
2. Ensure you have Python 3.8+ installed.
3. Install the required dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib

## Data Source
The historical stock market data used in this project is the **NIFTY-50 dataset**. Due to GitHub's file size limits and best practices, the massive master dataset is not hosted directly in this repository.

Please download the `NIFTY50_all.csv` file directly from Kaggle:
👉 **[Download NIFTY-50 Stock Market Data Here](https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data/data)**

**Setup Instructions:**
1. Download the archive from the Kaggle link above.
2. Extract the ZIP file.
3. Move the `NIFTY50_all.csv` file into the root directory of this project alongside `main.py` and `stock_metadata.csv`.
