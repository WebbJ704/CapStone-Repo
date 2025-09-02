# Portfolio Optimization with Random Forest and SciPy  

This project is a **quantitative finance pipeline** for stock portfolio optimization. It combines **data acquisition, statistical analysis, machine learning, and numerical optimization** to identify portfolio weights that maximize performance metrics like the **Sharpe ratio**.  

It also includes a **GitHub Pages site** to present the project as a structured capstone report (Executive Summary, Introduction, Methods, Results, and Conclusion).  

---

## Features  

### 1. Data Acquisition  
- Fetches historical stock price data using `yfinance`.  
- Supports caching to CSV for faster repeated access.  

### 2. Statistical Analysis  
- Computes daily and annualized returns for individual stocks.  
- Uses **bootstrap simulations** to estimate distributions of returns, volatility, and Sharpe ratios.  

### 3. Portfolio Simulation  
- Generates thousands of random portfolios and calculates their **annualized returns, volatility, and Sharpe ratios**.  
- Visualizes risk vs. reward for various portfolio weight combinations.  

### 4. Machine Learning Optimization  
- Uses a **Random Forest Regressor** to predict Sharpe ratios from simulated portfolio weights.  
- Identifies top-performing weight combinations with the trained model.  

### 5. Numerical Optimization  
- Uses **SciPy’s `minimize`** to find optimal portfolio weights that maximize the Sharpe ratio.  
- Supports constraints like weight bounds and minimum return requirements.  

### 6. Visualization  
- Plots distributions of returns, volatility, and Sharpe ratios from bootstrap simulations.  
- Visualizes cumulative returns of individual stocks and optimized portfolios.  

---

## Technologies & Libraries  

- Python 3  
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
- `scikit-learn` for Random Forest modeling  
- `scipy.optimize` for portfolio optimization  
- `yfinance` for historical stock data  
- `tqdm` for progress tracking  

---

## Typical Workflow  

1. Fetch historical stock data for desired tickers.  
2. Calculate daily returns and perform bootstrap analysis.  
3. Simulate thousands of random portfolios and compute performance metrics.  
4. Train a Random Forest model to predict Sharpe ratios from portfolio weights.  
5. Optimize portfolio weights with SciPy for maximum Sharpe ratio.  
6. Visualize results and cumulative returns.  

---

## Capstone Website (GitHub Pages)  

This repo also contains a **GitHub Pages site** for publishing the project in a structured format, suitable for academic or professional presentation.  

### Site Structure  

```
.
├─ _config.yml           # Jekyll theme and metadata
├─ index.md              # Executive Summary
├─ intro.md              # Introduction & Background
├─ methods.md            # Methods
├─ results.md            # Results
├─ conclusion.md         # Conclusion & Next Steps
├─ README.md             # This file
└─ assets/               # Charts, figures, tables
   ├─ risk_return.png
   ├─ bootstrap_sharpe.png
   ├─ cum_returns_rf.png
   └─ cum_returns_slsqp.png
```

### How to Use  

1. Place exported plots (from your Python scripts) into the `assets/` folder.  
2. Update the Markdown files (`index.md`, `methods.md`, etc.) with your actual results.  
3. Commit and push to GitHub.  
4. Enable **GitHub Pages** in your repo settings (`Settings → Pages → Source: main branch, / root`).  

Your site will be live at:  
```
https://<your-username>.github.io/<repo-name>/
```

---

## Exporting Figures from Python to Assets  

When running your analysis, save each figure directly into the `assets/` folder so it appears on the GitHub Pages site:  

```python
plt.savefig("assets/risk_return.png", dpi=200, bbox_inches="tight")
plt.savefig("assets/bootstrap_sharpe.png", dpi=200, bbox_inches="tight")
plt.savefig("assets/cum_returns_rf.png", dpi=200, bbox_inches="tight")
plt.savefig("assets/cum_returns_slsqp.png", dpi=200, bbox_inches="tight")
```

You can then embed them in your Markdown files like this:  

```markdown
![Risk vs Return](/assets/risk_return.png)  
![Bootstrap Sharpe Distribution](/assets/bootstrap_sharpe.png)  
![Cumulative Returns – Random Forest](/assets/cum_returns_rf.png)  
![Cumulative Returns – SLSQP](/assets/cum_returns_slsqp.png)  
```

---

The repo acts as both:  
- a **codebase** (quantitative finance pipeline), and  
- a **capstone report website** (professional presentation).  
