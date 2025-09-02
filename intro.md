---
layout: default
title: Introduction & Background
permalink: /intro.html
---

# Introduction & Background

## Context
Portfolio optimisation is a cornerstone of modern investment management. This project evaluates strategies for allocating capital among four major US technology stocks — Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), and AMD (AMD) — over the period 2020 to present.  

The goal is to design portfolios that maximise risk-adjusted returns (Sharpe ratio) and generalise well out of sample.  

## Research Question
**How can we allocate capital across AAPL, MSFT, GOOGL, and AMD to maximise out-of-sample Sharpe ratio, and how do machine learning and optimisation approaches compare?**  

## Motivation for a Data-Driven Solution
Financial returns are noisy, volatile, and highly dependent on sample windows. Classical mean–variance optimisation is sensitive to estimation error, which can result in extreme or unstable weights.  

This project introduces two data-driven techniques:  
- **Random Forest meta-modelling**: leveraging non-linear relationships between portfolio weights and Sharpe ratio.  
- **SLSQP optimisation**: solving directly for weights that maximise Sharpe under realistic constraints.  

## Contribution
- A reproducible Python workflow for portfolio optimisation.  
- Comparative evaluation of machine learning and numerical optimisation approaches.  
- Visual and statistical communication of uncertainty to decision-makers.

## Full Report

- [Executive Summary](/index.md)  
- [Introduction & Background](/intro.md)  
- [Methods](/methods.md)  
- [Results](/results.md)  
- [Conclusion & Next Steps](/conclusion.md)
