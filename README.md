🪙 Gold Price Prediction
📝 Project Overview

This project predicts gold prices using historical financial data and machine learning techniques. The goal is to identify key factors influencing gold prices and build models that can forecast future trends to assist in investment and risk management.

🎯 Objectives

Perform EDA on gold price data and related financial indicators.

Identify correlations between gold prices and variables like stock indices, USD rates, crude oil prices.

Build predictive models to forecast gold prices.

Evaluate model accuracy and visualize results.

🗂️ Dataset

Source: Kaggle / Yahoo Finance (Gold Price, US Dollar Index, S&P 500, Crude Oil, Inflation).

Columns:

Date

Gold Price (USD/oz)

Open, High, Low, Close

Stock Index values (e.g., S&P 500, Nasdaq)

USD/INR, USD Index

Crude Oil prices

Rows: ~5,000+ daily records.

File format: .csv

🔧 Tools & Technologies

Python → Pandas, NumPy, Matplotlib, Seaborn

Machine Learning → Scikit-learn (Linear Regression, Random Forest, XGBoost)

Statsmodels → Time Series (ARIMA, SARIMA)

Visualization → Matplotlib, Seaborn

Jupyter Notebook for analysis

📈 Methodology

Data Cleaning

Handle missing values

Convert date column to datetime & set as index

Normalize numerical features

EDA

Gold price trends over time

Correlation heatmap with external variables

Moving averages (30-day, 90-day)

Feature Engineering

Rolling mean / volatility features

Lag features for time series prediction

Model Building

Linear Regression → baseline model

Random Forest & XGBoost → non-linear regression

ARIMA/SARIMA → time series forecasting

Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

📊 Key Insights

Gold prices are inversely correlated with USD index.

Crude oil fluctuations also influence gold demand.

XGBoost outperformed linear models with lower RMSE.

Moving average smoothing improved time series stability.

📌 Outcomes

Built a gold price prediction model with R² ≈ 0.85.

Identified key drivers: USD index, crude oil, stock indices.

Forecast visualizations show short-term predictability but long-term volatility.

🚀 Future Work

Deploy as a Streamlit app for interactive predictions.

Integrate LSTM / Deep Learning models for time series.

Automate daily price updates using APIs (Yahoo Finance).
