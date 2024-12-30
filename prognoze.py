import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def forecast_currency(df, currency_name, forecast_periods=365):
    coin = df[[currency_name]].copy()
    coin['Date'] = df.index
    coin.set_index('Date', inplace=True)
    coin[currency_name].ffill(inplace=True)

    X = coin.index.astype(np.int64).values.reshape(-1, 1)
    y = coin[currency_name].values
    model = LinearRegression()
    model.fit(X, y)

    forecast = model.predict(X)
    forecast_df = pd.DataFrame(forecast, index=coin.index, columns=['Forecast'])
    future_dates = pd.date_range(coin.index[-1], periods=forecast_periods, freq='D')
    future_X = future_dates.astype(np.int64).values.reshape(-1, 1)
    future_forecast = model.predict(future_X)
    future_forecast_df = pd.DataFrame(future_forecast, index=future_dates, columns=['Forecast'])

    plt.plot(coin.index, coin[currency_name], label='Istorinės vertės', color='blue')
    plt.plot(forecast_df.index, forecast_df['Forecast'], label='Praeities tendencija', color='orange')
    plt.plot(future_forecast_df.index, future_forecast_df['Forecast'], label='Prognozuojama kainos', color='red')
    plt.title('Kriptovaliutos kainos prognozavimas')
    plt.xlabel('Data')
    plt.xticks(rotation=45, fontsize=7)
    plt.ylabel('Kaina (USD)')
    plt.grid(True)
    plt.legend()
    plt.show()

    return forecast_df, future_forecast_df