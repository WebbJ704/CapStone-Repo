---
layout: default
title: Conclusion & Next Steps
permalink: /conclusion.html
---

## Conclusion & Next Steps

### Summary
Two approaches for portfolio optimization were demonstrated and compared based on their out-of-sample performance from **2024-01-01** onward.  

- Using a randomly selected weighting from the top 20 Sharpe ratios produced by the **Random Forest model** resulted in an increase in Sharpe ratio of **0.07** compared to the SciPy optimization model.  
- Both models achieved a Sharpe of **~0.92** on the training data.  
- On the test data, the Random Forest portfolio was only **23% below the training Sharpe**, whereas the SciPy-optimized portfolio was **30% below**, indicating that the Random Forest model provides more robust out-of-sample performance.  
- **Bootstrapping** provided uncertainty bounds, increasing confidence in the findings.  

---

### Recommendations
- Incorporate additional data sources (e.g., **risk-free rate, macroeconomic indicators**) to contextualize performance.  
- Introduce **rolling or expanding window validation** and account for **transaction costs**.  
- Explore alternative models (e.g., **Gradient Boosting, Bayesian optimization**) and additional constraints (e.g., **sector caps, maximum weight limits**).  

---

### Limitations
- **Survivorship bias** and limited asset universe may affect generalizability.  
- Results are sensitive to **parameter choices**, such as look-back window and resampling seed.  
- The current pipeline **does not account for transaction costs or slippage**.


## Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
