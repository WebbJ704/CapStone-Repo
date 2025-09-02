import CapStoneV4 as CS
import pandas as pd

# ----------------- INNSTRUMENT CONFIG -----------------
SYMBOL = ['AAPL', 'MSFT', 'GOOGL','AMD']
initial_investment = 1
# ------------------------------------------------------
if __name__ == "__main__":
    # ----------------- Data Acquisition & Preprocessing -----------------
    df = {}
    df_return = {}
    for ticker in SYMBOL:
        data = CS.fetch_yf_data(ticker, '2020-01-18') #This is the start date of where you want data to be at
        df[f'{ticker} Adj Close'] = data['Close']
        df[f'{ticker} Return'] = data['Close'].pct_change()
        df_return[f'{ticker}'] = data['Close'].pct_change()
    df =pd.DataFrame(df)
    df.dropna(inplace =True) 
    df_return = pd.DataFrame(df_return)
    df_return.dropna(inplace = True)

    # ----------------- Single stock Performance Evaluation / Statistical Analysis -----------------

    # Split data chronologically
    train_df = df[df.index < '2024-01-01'].copy()
    test_df = df[df.index >= '2024-01-01'].copy() 
    train_return_df = df_return[df_return.index < '2024-01-01'].copy()
    test_return_df = df_return[df_return.index >= '2024-01-01'].copy()

    # Bootstrap Whole data to better understand each stock for whole dataset
    Bootstrap_results =  CS.bootstrap(df, SYMBOL)
    CS.plot_bootstrap(Bootstrap_results, SYMBOL)

    #Determin Anualised shapre for each stock on whole dataset
    Anualised_sharp = CS.Anualised_sharpe(df,SYMBOL)
 
    #----------------- Portfolio Performance of different weights -----------------  
       
    #spread of weights, risk , retrun which can be used ti determin min retrun constrain for Scipy minimise alos data for model
    data_train = CS.weights_perfromace_plot(train_return_df, SYMBOL, iter = 10000)

    # ----------------- portfolio Performance Evaluation with RandomForest Modeling -----------------    

    #Use Random forest modeling to predict best weights to maximise sharpe ratio
    weights_model, sharpe_model = CS.RandomForest(data_train, SYMBOL, n_samples = 10000)
    weights_str = ", ".join([f"{t}: {w:.2f}" for t, w in zip(SYMBOL, weights_model)])
    print('Sharpe Ratio predicted by model on train data', sharpe_model)
    print("Model weights Randomly selected from Top 20 to avoid overfitting:", weights_str)
   
    #run models through evaluatating pipile on test df and whole df
    anual_sharpe_train_model, Porfolio_Returns_train_model = CS.portfolio_performance_pipeline(train_df,weights_model, SYMBOL)
    anual_sharpe_test_model, Porfolio_Returns_test_model = CS.portfolio_performance_pipeline(test_df,weights_model, SYMBOL)
    print(f'Anualsied sharpe on Train data of sampled weights from model', anual_sharpe_train_model)
    print(f'Anualsied sharpe on Test data of sampled weights from model', anual_sharpe_test_model)
    print(f'Return on Train data of sampled weight from model', initial_investment + Porfolio_Returns_train_model.sum())
    print(f'Return on Test data of sampled weights from model', initial_investment  + Porfolio_Returns_test_model.sum())

    # run the bootstrap on the optimal weights return from random forest on test data and whole data
    Bootstrap_results_train_model =  CS.bootstrap_weighted(Porfolio_Returns_train_model)
    Bootstrap_results_test_model =  CS.bootstrap_weighted(Porfolio_Returns_test_model)
    CS.plot_bootstrap_weights(Bootstrap_results_train_model, SYMBOL, weights_model,'Train Data returns: Model Weights')
    CS.plot_bootstrap_weights(Bootstrap_results_test_model, SYMBOL, weights_model,'Test Data returns: Model Weights')

    #plot the cumulative retruns of each stock vs portfolio weighted return
    CS.cumulative_return_plot(df,Porfolio_Returns_train_model, SYMBOL, weights_model, "Cumulative Return: sampled weights from Random Forest Model on train Dataset")
    CS.cumulative_return_plot(test_df,Porfolio_Returns_test_model, SYMBOL, weights_model, 'Cumulative Return: sampled weights from Random Forest Model on test Dataset')

       
    # ----------------- portfolio Performance Evaluation with scipy minimise with a min return constrain -----------------    

    # scipiy optimise on train data then input weights into test data
    sharpe_scipy , weights_scipy = CS.optimise(train_return_df, SYMBOL, risk_free_rate=0.02, min_return=0.25)
    weights_str_scipy = ", ".join([f"{t}: {w:.2f}" for t, w in zip(SYMBOL, weights_scipy)])
    print('Sharpe from Scipy',sharpe_scipy)
    print('weight from scipy',weights_str_scipy)

    anual_sharpe_train_scipy, Porfolio_Returns_train_scipy = CS.portfolio_performance_pipeline(train_df,weights_scipy, SYMBOL)
    anual_sharpe_test_scipy, Porfolio_Returns_test_scipy = CS.portfolio_performance_pipeline(test_df,weights_scipy, SYMBOL)
    print(f'Anualsied sharpe on train data of optimised weights from scipy', anual_sharpe_train_scipy)
    print(f'Anualsied sharpe on Test data of optimised weights from scipy', anual_sharpe_test_scipy)
    print(f'Return on train data of optimised weights from scipy', initial_investment + Porfolio_Returns_train_scipy.sum())
    print(f'Return on Test data of optimised weights from scipy', initial_investment + Porfolio_Returns_test_scipy.sum())

    # run bootsrap on retruns on train returns and test returns using scipy weights
    Bootstrap_results_train_scipy =  CS.bootstrap_weighted(Porfolio_Returns_train_scipy)
    Bootstrap_results_test_scipy =  CS.bootstrap_weighted(Porfolio_Returns_test_scipy)
    CS.plot_bootstrap_weights(Bootstrap_results_train_scipy, SYMBOL, weights_scipy, 'Train Data returns: scipy Weights')
    CS.plot_bootstrap_weights(Bootstrap_results_test_scipy, SYMBOL, weights_scipy, 'Test Data returns: scipy Weights')
   
    #plot the cumulative retruns of each stock vs portfolio weighted return
    CS.cumulative_return_plot(train_df,Porfolio_Returns_train_scipy, SYMBOL, weights_scipy, 'Cumulative Return: optimal weights from scipy Study on train Dataset')
    CS.cumulative_return_plot(test_df,Porfolio_Returns_test_scipy, SYMBOL, weights_scipy, 'Cumulative Return: optimal weights from scipy Study on test Dataset') 
   