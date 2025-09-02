---
layout: default
title: Conclusion & Next Steps
permalink: /conclusion.html
---

# Conclusion & Next Steps

## Summary
- Two appreaches have been demonstrated for portfolio optimisation and compared their out‑of‑sample performance from 2024‑01‑01 onward.
- It was found that by using an randomly selected weighting from the top 20 shapre ratios prudced by the random forest model gave an increase in sharpe by 0.07 than that of the scipy model. both models had a sharpe of **[0.92]** on the train data. therefore both models still are off but the radnom forest is only off by 23% where scipy is off by 30% making the random forest the better choice.
- Bootstrapping provided uncertainty bounds, improving the credibility of the findings.

## Recommendations
1. Add a second data source (risk‑free or macro) to contextualise performance.  
2. Introduce rolling/expanding window validation and transaction costs.  
3. Consider alternative models (e.g., Gradient Boosting, Bayesian optimisation) and constraints (sector caps, max weight).

## Limitations
- Survivorship bias and limited asset universe.  
- Parameter sensitivity (look‑back window, resampling seed).  
- No transaction costs or slippage in current pipeline.

## Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
