from cProfile import label
from pickle import FALSE
from statistics import correlation
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.vector_ar.var_model import forecast
from sklearn.linear_model import LinearRegression
from load_crypto import get_cryptos
from prognoze import forecast_currency

# nurodau kokiu valiutu kainas noriu matyti grafike
df = get_cryptos(['Aave','Celo'])

# nurodau tarp kuriu valiutu ieskau rysio
x = df['Aave']
y = df['Celo']
correlation = df.corr()

# nurodau kokios valiutos verte spesiu
currency_name = 'Celo'

                                         # RODYTI JAU TURIMAS VERTES
# averages = df.mean()
# minimums = df.min()
# maximums = df.max()
# df.plot()
# plt.title('Kriptovaliutų kainos')
# plt.xlabel('Data')
# plt.ylabel('Kaina USD')
# plt.legend(labels=[f'{currency} Vidurkis: {averages[currency]:.2f}, Min: {minimums[currency]:.2f}, Max: {maximums[currency]:.2f}' for currency in df.columns])
# plt.show()
                                        # RODYTI KORELIACIJA

plt.scatter(x=x,y=y, color = 'blue', alpha = 0.5, label ='Points')
sns.regplot(x=x, y=y,  scatter = False, color = 'red', line_kws={"linewidth":2}, label= 'Koreliacijos linija')
plt.title('Koreliacija tarp valiutų')
plt.show()
                                          # RODYTI SPEJIMA

# forecast_df, future_forecast_df = forecast_currency(df, currency_name, forecast_periods=365)
