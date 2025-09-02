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
![Individual assets statistics](https://username.github.io/CapStone-Repo/assets/bootstrap_individual_assets.png)


## Random Forest Results
- Train R²: **[0.9995]**;  
- Test R²: **[0.9975]**  
- Selected test portfolio weights from top 20 to avoid over fitting: **[AAPL: 0.44, MSFT: 0.37, GOOGL: 0.00, AMD: 0.19]**
- Predicted train Sharpe: **[0.92]** 
- Predicted test Sharpe: **[0.71]**  

**Random Forest Figures:**  
- ![Risk vs Return](/assets/risk%20retrun.png)  
- ![Test Boostrap Distributions](/assets/Test%20Data%20returns:%20Model%20Weights.png)  
- ![Test Cumulative Returns – RF](/assets/Cumulative%20Return:%20sampled%20weights%20from%20Random%20Forest%20Model%20on%20test%20Dataset.png)  

## SLSQP Optimisation Results
- Optimal test weights: **[AAPL: 0.50, MSFT: 0.26, GOOGL: 0.00, AMD: 0.24]**
- Train Sharpe: **[0.92]**
- Test Sharpe: **[0.64]**   

**SLSQP Figures:**  
- ![Test Boostrap Distributions - SLSQP](/assets/Test%20Data%20returns:%20scipy%20Weights.png) 
- ![Test Cumulative Returns – SLSQP](/assets/Cumulative%20Return:%20optimal%20weights%20from%20scipy%20Study%20on%20test%20Dataset.png)  

## Discussion and Interpretation of Results

### 1. Individual Stock Performance
The annualized Sharpe ratios for the individual stocks indicate their risk-adjusted performance over the period considered:  
- **MSFT (0.8452)** and **AAPL (0.7639)** showed the highest risk-adjusted returns.  
- **GOOGL (0.7177)** and **AMD (0.6627)** had lower Sharpe ratios, suggesting relatively less efficient reward per unit of risk.  

This provides a baseline understanding of each stock’s standalone performance before portfolio optimization.

### 2. Portfolio Simulation and Random Forest Model
A large number of random portfolios (10,000) were simulated to explore possible weight combinations.  
- The **Random Forest model** achieved high R² values on both train (0.9995) and test (0.9975) sets, indicating it can accurately predict the Sharpe ratio from portfolio weights.  
- The low MSE (≈2e-6) and MAE (≈0.00089) confirm the model’s precision.  

The **model-selected portfolio weights** were:  
- **AAPL: 0.44, MSFT: 0.37, GOOGL: 0.00, AMD: 0.19**  

Performance of these weights:  
- **Train Sharpe:** 0.924, **Train return:** 2.203  
- **Test Sharpe:** 0.708, **Test return:** 1.293  

> Interpretation: The model performs well on training data, but the drop on test data suggests some overfitting or sensitivity to unseen market conditions.

### 3. SciPy Optimization
Using numerical optimization to maximize Sharpe ratio, the resulting weights were:  
- **AAPL: 0.50, MSFT: 0.26, GOOGL: 0.00, AMD: 0.24**  

Performance of these weights:  
- **Train Sharpe:** 0.925, **Train return:** 2.237  
- **Test Sharpe:** 0.645, **Test return:** 1.285  

> Interpretation: SciPy optimization produced similar train performance as the Random Forest model, but slightly lower test Sharpe, highlighting sensitivity to out-of-sample data.

### 4. Comparative Insights
- Both methods assign **zero weight to GOOGL**, suggesting it contributes little to risk-adjusted returns in this portfolio.  
- Portfolios are heavily weighted toward **AAPL and MSFT**, reflecting their higher standalone Sharpe ratios.  
- The drop from train to test Sharpe emphasizes the importance of evaluating portfolio robustness on unseen data.

### 5. Overall Conclusion
- Combining **simulation, machine learning, and optimization** provides a robust framework for portfolio construction.  
- The **Random Forest model** allows rapid evaluation of many weight combinations, while **SciPy optimization** offers a principled numerical approach.  
- Monitoring test set performance is essential to mitigate overfitting and ensure portfolio generalization.


## Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
