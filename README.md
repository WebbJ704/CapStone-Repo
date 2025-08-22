# My-Program-Repo

# Portfolio Optimization with Random Forest and SciPy

This project is a **quantitative finance pipeline** for stock portfolio optimization. It combines **data acquisition, statistical analysis, machine learning, and numerical optimization** to identify portfolio weights that maximize performance metrics like the **Sharpe ratio**.

## Features

1. **Data Acquisition**  
   - Automatically fetches historical stock price data using `yfinance`.  
   - Supports caching to CSV for faster repeated access.  

2. **Statistical Analysis**  
   - Computes daily and annualized returns for individual stocks.  
   - Uses **bootstrap simulations** to estimate distributions of returns, volatility, and Sharpe ratios.  

3. **Portfolio Simulation**  
   - Generates thousands of random portfolios and calculates their **annualized returns, volatility, and Sharpe ratios**.  
   - Visualizes risk vs. reward for various portfolio weight combinations.  

4. **Machine Learning Optimization**  
   - Uses a **Random Forest Regressor** to predict Sharpe ratios from simulated portfolio weights.  
   - Identifies top-performing weight combinations with the trained model.  

5. **Numerical Optimization**  
   - Uses **SciPy’s `minimize`** to find optimal portfolio weights that maximize the Sharpe ratio.  
   - Supports constraints like weight bounds and minimum return requirements.  

6. **Visualization**  
   - Plots distributions of returns, volatility, and Sharpe ratios from bootstrap simulations.  
   - Visualizes cumulative returns of individual stocks and optimized portfolios.  

## Technologies & Libraries

- Python 3  
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
- `scikit-learn` for Random Forest modeling  
- `scipy.optimize` for portfolio optimization  
- `yfinance` for historical stock data  
- `tqdm` for progress tracking  

## Typical Workflow

1. Fetch historical stock data for desired tickers.  
2. Calculate daily returns and perform bootstrap analysis.  
3. Simulate thousands of random portfolios and compute performance metrics.  
4. Train a Random Forest model to predict Sharpe ratios from portfolio weights.  
5. Optimize portfolio weights with SciPy for maximum Sharpe ratio.  
6. Visualize results and cumulative returns.
