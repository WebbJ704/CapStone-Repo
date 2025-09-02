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
![Individual assests statistics](/assets/bootstrap%20individual%20assets.png)  

## Random Forest Results
- Train R²: **[0.9995]**;  
- Test R²: **[0.9969]**  
- Selected test portfolio weights from top 20 to avoid over fitting: **[AAPL: 0.45, MSFT: 0.31, GOOGL: 0.01, AMD: 0.24]**  
- Predicted test Sharpe: **[0.67]**  

**Random Forest Figures:**  
- ![Risk vs Return](/assets/risk%20retrun.png)  
- ![Test Boostrap Distributions](/assets/Test%20Data%20returns:%20Model%20Weights.png)  
- ![Test Cumulative Returns – RF](/assets/Cumulative%20Return:%20sampled%20weights%20from%20Random%20Forest%20Model%20on%20test%20Dataset.png)  

## SLSQP Optimisation Results
- Optimal test weights: **[AAPL: 0.50, MSFT: 0.26, GOOGL: 0.00, AMD: 0.24]**  
- Test Sharpe: **[0.64]**   

**SLSQP Figures:**  
- ![Test Boostrap Distributions - SLSQP](/assets/Test%20Data%20returns:%20scipy%20Weights.png) 
- ![Test Cumulative Returns – SLSQP](/assets/Cumulative%20Return:%20sampled%20weights%20from%20scipy%20FStudy%20on%20test%20Dataset.png)  

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
