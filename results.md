---
layout: default
title: Results
permalink: /results.html
---

# Results

## Descriptive Statistics
Graph provides a summary of bootstraped statistics for each stock:  
- Mean daily/annualised returns  
- Volatility  
- Sharpe ratio
- ![Individual assests statistics](/assets/bootstrap individual assests.png)  

## Random Forest Results
- Train R²: **[…]**; Cross-validation mean ± std: **[…]**  
- Test R²: **[…]**  
- Selected test portfolio weights: **[…]**  
- Predicted test Sharpe: **[…]**  

**Figures:**  
- ![Risk vs Return](/assets/risk_return.png)  
- ![Sharpe Distribution (Bootstrap)](/assets/bootstrap_sharpe.png)  
- ![Cumulative Returns – RF](/assets/cum_returns_rf.png)  

## SLSQP Optimisation Results
- Optimal test weights: **[…]**  
- Test Sharpe: **[…]**  
- Bootstrap mean Sharpe: **[…]**, 95% CI: **[…, …]**  

**Figures:**  
- ![Cumulative Returns – SLSQP](/assets/cum_returns_slsqp.png)  

## Interpretation
- Compare Random Forest vs SLSQP performance.  
- Comment on stability of weights and robustness across train/test.  
- Highlight where results diverged and what that means in practice.

## Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
