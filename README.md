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