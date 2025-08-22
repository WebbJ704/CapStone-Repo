# run a load of oiterations to make datset then use random forest to optimise. then use scipy and compare

import yfinance as yf
import pandas as pd 
import os
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from scipy.optimize import minimize
from tqdm import tqdm
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, classification_report, confusion_matrix

# ----------------- Data Acquisition & Preprocessing -----------------
def fetch_yf_data(ticker, start = '2020-09-18', end = date.today().strftime("%Y-%m-%d")):
    filename = f'{ticker}_data.csv'
    
    if os.path.exists(filename):
        print(f"{filename} already exists. Loading from disk...")
        df = pd.read_csv(filename)
        df.reset_index(inplace=True) 
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")
        df = df[(df.index >= pd.to_datetime(start)) & (df.index <= pd.to_datetime(end))]
        return df
    else:
        print(f"Downloading data for {ticker}...")
        data = yf.download(ticker, period="max", interval="1d", auto_adjust=True)
        data.reset_index(inplace=True) 
        df = data[["Date", "Open", "High", "Low", "Close", "Volume"]]
        df.columns = ["date", "Open", "High", "Low", "Close", "Volume"]
        df["date"] = pd.to_datetime(df["date"]) 
        df = df.set_index("date")
        df.to_csv(filename)
        df = df[(df.index >= pd.to_datetime(start)) & (df.index <= pd.to_datetime(end))]
        return df
    
# ----------------- Single stock Performance Evaluation / Statistical Analysis -----------------

def bootstrap(df, tickers, n_simulations=1000):
    bootstrap_results = [] 
    for ticker in tickers:
        for i in range(n_simulations):
            sample = df[f'{ticker} Return'].sample(len(df), replace = True, random_state = i)
            sample_mean = sample.mean()
            sample_std = sample.std()
            sharpe = sample_mean/sample_std * np.sqrt(252)
            bootstrap_results.append({ "ticker": ticker,
                             "c0_means":sample_mean,
                            "c0_dev":sample_std,
                            "sharpe":sharpe})
    results = pd.DataFrame(bootstrap_results)
    return results

def Anualised_sharpe(df,tickers):
    Anual_sharpe = []
    for ticker in tickers:
        mean_return = df[f'{ticker} Return'].mean()
        std_return = df[f'{ticker} Return'].std()
        Anual_sharpe.append({'stock': ticker,
                              "Anlualised Shapre": mean_return/std_return*np.sqrt(256) }) 
        print(f"Anualised Sharpe Ratio for {ticker}: {mean_return/std_return*np.sqrt(256):.4f}")
    return Anual_sharpe


# ----------------- portfolio Performance of different weights -----------------    
def weights_perfromace_plot(df, tickers, iter=1000):
    means = []
    risks = []
    w = []
    sharpe = []
    dataframe = []
    n = len(tickers)

    for i in tqdm(range(iter), desc="Simulating portfolios"):
        weights = np.random.random(size=n)
        weights = weights / sum(weights)

        returns = df.mean()
        mu = returns @ weights
        c = df.cov()

        sigma = np.sqrt(weights @ c @ weights.T)
        sigma_anual = sigma * np.sqrt(252)
        mu_anual = mu * 252
        sharpe_anual = mu_anual / sigma_anual

        sharpe.append(sharpe_anual)
        means.append(mu_anual)
        risks.append(sigma_anual)
        w.append(weights)
        dataframe.append({'sharpe': sharpe_anual,
                          'weights': weights})

    plt.scatter(risks, means, alpha=0.4, edgecolor='black')
    plt.title(f'Risk vs. reward of different portfolios for {tickers}')
    plt.grid()
    plt.xlabel('Annualised Volatility')
    plt.ylabel('Annualised Returns')
    plt.show()

    return pd.DataFrame(dataframe)


# ----------------- portfolio Performance Pipeline and statistical anlaysis -----------------   

def  portfolio_performance_pipeline(df,weights,tickers):
    weights = np.array(list(weights))
    weights = weights/sum(weights)
    if not np.isclose(weights.sum(), 1.0):
        raise ValueError("Weights must sum to 1.")
    
    # Extract return columns
    return_cols = [f"{ticker} Return" for ticker in tickers]
    returns = df[return_cols].dropna()

    # Daily portfolio returns
    portfolio_returns = returns.dot(weights)

    # Calculate performance metrics
    mean_daily_return = portfolio_returns.mean()
    std_daily_return = portfolio_returns.std()

    #Anualsied sharpe ratio
    sharpe_ratio = mean_daily_return/ std_daily_return * np.sqrt(252)
    return sharpe_ratio , portfolio_returns

def bootstrap_weighted(df, n_simulations=1000):
    bootstrap_results = [] 
    for i in range(n_simulations):
        sample = df.sample(len(df), replace = True, random_state = i)
        sample_mean = sample.mean()
        sample_std = sample.std()
        sharpe = sample_mean/sample_std * np.sqrt(252)
        bootstrap_results.append({"c0_means":sample_mean,
                            "c0_dev":sample_std,
                            "sharpe":sharpe})
    return bootstrap_results


# ----------------- portfolio Performance Evaluation with RandomForest Modeling -----------------    

def RandomForest(res_df,tickers, n_samples = 100000):
    # Expand list of weights into columns
    weights_df = pd.DataFrame(res_df['weights'].to_list(), index=res_df.index)
    weights_df.columns = [f"w{i}" for i in range(weights_df.shape[1])]

    X = weights_df
    y = res_df['sharpe']
    # Drop bad trials
    X = X[y.notna()]
    y = y[y.notna()]
    
    #Split into test and train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=22)
    
    #Initalise and fit model
    model = RandomForestRegressor(n_estimators=100, random_state=22)
    model.fit(X_train,y_train)

    #Model scores 
    train_score = model.score(X_train, y_train)
    print(f"Random Forest R^2 on train set: {train_score:.4f}")
    test_score = model.score(X_test, y_test)
    print(f"Random Forest R^2 on test set: {test_score:.4f}")
    forest_scores =cross_val_score(model,X_train,y_train,cv=5)
    print(f'The average accuracy for the forest was: {forest_scores.mean(): .4f} and deviations {forest_scores.std(): .3f}') 
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("MSE:", mse)
    print("MAE:", mae)
    print("R²:", r2)
    
    # Number of new samples and parameter count
    n_params = len([col for col in X.columns if col.startswith("w")])  # based on training

    new_params_list = []
    for i in range(n_samples):
        #Creates weights to map onto model
        weights = np.random.random(size = len(tickers))
        weights /= weights.sum()  
        new_params_list.append(weights)

    # Create DataFrame
    
    X_new = pd.DataFrame(new_params_list)
    X_new.columns = [f"w{i}" for i in range(X_new.shape[1])]
 
    #Predict over new params
    predicted_sharpes = model.predict(X_new)
    X_new['predicted_sharpe'] = predicted_sharpes  
    top_20 = X_new.sort_values(by='predicted_sharpe', ascending=False).head(20)

    # Randomly select 1 row to avoid over fitting
    sampled_row = top_20.sample(n=1, random_state=42).iloc[0]

    sharpe_model = sampled_row['predicted_sharpe']
   
    # Extract number of weight parameters (w_0 to w_{n-2})
    n_params = len([col for col in top_20.columns if col.startswith("w")])
    weights_model = [sampled_row[f"w{i}"] for i in range(n_params)]

    return weights_model, sharpe_model

# ----------------- portfolio Performance Evaluation with scipy optimise -----------------    

def neg_sharpe(weights, mean_returns, cov_matrix, risk_free_rate):
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    if portfolio_volatility == 0:
        return 1e6  # large penalty to avoid division by zero
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return -sharpe_ratio  # negative for minimization

def optimise(stocks, tickers, risk_free_rate=0.00, min_return=None):
    n = len(tickers)
    trading_days = 252

    # Annualized stats
    mean_returns = stocks.mean() * trading_days
    cov_matrix = stocks.cov() * trading_days

    # Bounds: no short selling, max 100% per asset
    bounds = [(0.0, 1.0)] * n

    # Constraints
    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    
    if min_return is not None:
        constraints.append({
            'type': 'ineq',
            'fun': lambda w: np.dot(w, mean_returns) - min_return
        })

    # Starting guess: evenly distributed
    initial_weights = np.ones(n) / n

    result = minimize(
        neg_sharpe,
        initial_weights,
        args=(mean_returns, cov_matrix, risk_free_rate),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'disp': False}
    )

    # Return Sharpe (positive) and weights
    optimal_sharpe = -result.fun
    optimal_weights = result.x
    return optimal_sharpe, optimal_weights

# ----------------- Data Visualization -----------------
def get_bins(data):
    n = len(data)
    return min(max(int(np.sqrt(n)), 10), 100) 

def plot_bootstrap(results, tickers):
    n = len(tickers)
    fig3, ax3 = plt.subplots(n, 3, figsize=(20, 4 * n))  # One row per ticker

    if n == 1:
        ax3 = np.expand_dims(ax3, axis=0)  # Make sure it's always 2D

    for i, ticker in enumerate(tickers):
        data = results.groupby('ticker').get_group(ticker)

        # Plot c0_means
        sns.histplot(data['c0_means']*252, bins=get_bins(data['c0_means']), kde=True, ax=ax3[i][0], label=ticker)
        if i == 0:
            ax3[i][0].set_title('Distribution of Anual System Return Means')
        ax3[i][0].legend()

        # Plot c0_dev
        sns.histplot(data['c0_dev']*np.sqrt(252), bins=get_bins(data['c0_dev']), kde=True, ax=ax3[i][1], label=ticker)
        if i == 0:
            ax3[i][1].set_title('Distribution of Anual Return Standard Deviations')
        ax3[i][1].legend()

        # Plot Sharpe
        sns.histplot(data['sharpe'], bins=get_bins(data['sharpe']), kde=True, ax=ax3[i][2], label=ticker)
        mean = np.mean(data['sharpe'])
        std = np.std(data['sharpe'])
        ax3[i][2].axvline(mean + 2 * std, linestyle='--', label='+2σ')
        ax3[i][2].axvline(mean - 2 * std, linestyle='--', label='-2σ')
        if i == 0:
            ax3[i][2].set_title('Distribution of Anualised Sharpe Ratios')
        ax3[i][2].legend()

    plt.tight_layout()
    plt.show()


def plot_bootstrap_weights(results,tickers,weights,title):
    # Helper function for title with weights
    weights = np.array(list(weights))
    weights = weights/sum(weights)
    weights_str = ", ".join([f"{t}: {w:.2f}" for t, w in zip(tickers, weights)])
    results = pd.DataFrame(results)
    fig3, ax3 = plt.subplots(1, 3, figsize=(20, 4))
    sns.histplot(results['c0_means']*256, bins=get_bins(results['c0_means']), kde=True, ax=ax3[0], label = weights_str)
    ax3[0].legend()
    ax3[0].set_title('Distribution of anual system return Means')
    sns.histplot(results['c0_dev']*np.sqrt(252), bins=get_bins(results['c0_dev']), kde=True, ax=ax3[1])
    ax3[1].set_title('Distribution of anual system retrun Standard Deviations')
    sns.histplot(results['sharpe'], bins=get_bins(results['sharpe']), kde=True, ax=ax3[2])
    ax3[2].axvline(np.mean(results['sharpe'])+ 2 * np.std(results['sharpe']), linestyle='--', label='+2σ')
    ax3[2].axvline(np.mean(results['sharpe']) - 2 * np.std(results['sharpe']), linestyle='--', label='-2σ')
    ax3[2].set_title(f'Dsitribution of system Anualised Sharp Ratios')
    ax3[2].legend()
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def cumulative_return_plot(df, df_weights, tickers, weights, title):
    weights = np.array(list(weights))
    weights = weights/sum(weights)
    weights_str = ", ".join([f"{t}: {w:.2f}" for t, w in zip(tickers, weights)])
    for ticker in tickers:
        plt.plot((1+df[f'{ticker} Return']).cumprod(), label = ticker)
    plt.plot((1+df_weights).cumprod(), label = weights_str)
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.legend()
    plt.title(title)
    plt.tight_layout()
    plt.show()



