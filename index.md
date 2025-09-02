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

## Key Results _(to be filled by you)_
- **Random Forest**: Predicted test Sharpe of **[X.XX]** with weights **[AAPL x.xx, MSFT x.xx, …]**.  
- **SLSQP**: Test Sharpe of **[Y.YY]** with weights **[…]** under a minimum return constraint of **[Z%]**.  
- **Bootstrap**: Mean Sharpe **[…]**, 95% interval **[…, …]**.  
- **Cumulative Return**: Portfolio achieved **[…]%** vs equal-weight benchmark **[…]%** in the test period.  

## Implications
The combined machine learning and optimisation framework demonstrates how uncertainty-aware portfolio construction can outperform naive benchmarks. Beyond finance, this approach generalises to other FP&A contexts — such as product mix, pricing, and budget allocation — where trade-offs and uncertainty must be managed.  

## Next Steps
- Add risk-free/macro data to improve Sharpe calculation.  
- Incorporate transaction costs and rebalancing.  
- Extend to rolling/expanding validation for robustness.  

---

## 📑 Full Report

- [Introduction & Background](/intro.html)  
- [Methods](/methods.html)  
- [Results](/results.html)  
- [Conclusion & Next Steps](/conclusion.html)
