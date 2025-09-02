---
layout: default
title: Methods
permalink: /methods.html
---

# Methods

## Data Sources
1. **Yahoo Finance (yfinance)**: Daily OHLCV for AAPL, MSFT, GOOGL, AMD from January 2020 to present.  
2. **(Optional second source)**: Risk-free rate (e.g., 3-Month US Treasury Bill from FRED) to calculate excess returns.  

## Data Pre-Processing
- Downloaded and stored local CSVs to avoid repeated API calls.  
- Calculated daily returns from adjusted close prices.  
- Split into **train set** (data before 2024-01-01) and **test set** (2024 onward).  
- Ensured no missing values after alignment of trading days.  

## Modelling Approaches

### Random Forest Meta-Model
- Sampled thousands of random weight vectors (long-only, sum to 1).  
- Computed Sharpe ratios for each portfolio in the train set.  
- Trained a `RandomForestRegressor` to predict Sharpe from weights.  
- Predicted Sharpe for new weight samples and selected a random allocation from the top 20 to reduce overfitting.  

### SLSQP Sharpe Optimisation
- Annualised mean returns and covariance matrix (252 trading days).  
- Objective: maximise Sharpe = (mean return – risk-free rate) / volatility.  
- Constraints:  
  - All weights ≥ 0 (no shorting).  
  - Weights sum to 1.  
  - Optional minimum return requirement.  
- Optimised weights applied to both train and test sets.  

### Bootstrap Resampling
- Resampled returns with replacement to estimate distributions of mean, volatility, and Sharpe.  
- Provided confidence intervals for portfolio performance.  

## Visualisation
- **Risk vs Return scatter**: distribution of Sharpe ratios across random portfolios.  
- **Bootstrap histograms**: distributions of annualised means, volatilities, and Sharpe.  
- **Cumulative return plots**: portfolio performance vs individual stocks and equal-weight benchmark.

## 📑 Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
