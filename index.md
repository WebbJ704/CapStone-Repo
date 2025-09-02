---
layout: default
title: Executive Summary
---

# Executive Summary

**Project Title:** Portfolio Optimisation & Forecasting of US Tech Equities (2020–Present)  
**Author:** James Webb  
**Date:** September 2025  

## Problem & Motivation
Investors face the challenge of constructing portfolios that balance return and risk under uncertainty. Traditional mean–variance optimisation is often unstable, leading to allocations that fail out of sample. This project applies both **machine learning** and **numerical optimisation** to build and evaluate portfolios of leading US technology equities (AAPL, MSFT, GOOGL, AMD).  

## Data & Methods
Daily adjusted close data was sourced from **Yahoo Finance** (via `yfinance`). Portfolios were evaluated using:  

- **Random Forest Regressor** trained on thousands of sampled weight vectors to predict Sharpe ratios and identify high-performing allocations.  
- **SLSQP Optimisation** (scipy) to directly maximise annualised Sharpe ratio with constraints (long-only, weights sum to 1).  
- **Bootstrapping** of returns to quantify uncertainty around performance metrics.  
- **Visualisation** of risk/return trade-offs and cumulative returns.  

## Key Results 
- **Random Forest**: Predicted test Sharpe of **[0.67]** with weights **[AAPL: 0.45, MSFT: 0.31, GOOGL: 0.01, AMD: 0.24]**.  
- **SLSQP**: Test Sharpe of **[0.64]** with weights **[AAPL: 0.50, MSFT: 0.26, GOOGL: 0.00, AMD: 0.24]** under a minimum return constraint of **[25%]**.  
- **Bootstrap Random Forest**: Mean Sharpe **[…]**, 95% interval **[…, …]**.
- **Bootstrap SLSQP**: Mean Sharpe **[…]**, 95% interval **[…, …]**. 
- **Cumulative Return Random Forest**: Portfolio achieved **[…]%** vs equal-weight benchmark **[…]%** in the test period.
- **Cumulative Return SLSQ**: Portfolio achieved **[…]%** vs equal-weight benchmark **[…]%** in the test period.  

## Implications
The combined machine learning and optimisation framework demonstrates how uncertainty-aware portfolio construction can outperform naive benchmarks. Beyond finance, this approach generalises to other FP&A contexts — such as product mix, pricing, and budget allocation — where trade-offs and uncertainty must be managed.  

## Next Steps
- Add risk-free/macro data to improve Sharpe calculation.  
- Incorporate transaction costs and rebalancing.  
- Extend to rolling/expanding validation for robustness.  

---

## 📑 Full Report

- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
