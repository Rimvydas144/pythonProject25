import pandas as pd
import matplotlib.pyplot as plt

def get_cryptos(titles):
    df_arr = []
    for title in titles:
        tmpDf = pd.read_csv(f'files/{title}.csv')
        tmpDf['Date'] = pd.to_datetime(tmpDf['Date'])
        tmpDf.set_index('Date', inplace=True)
        tmpDf = tmpDf[['Close']].rename(columns={'Close': title})

        df_arr.append(tmpDf)

    merged_df = df_arr[0].join(df_arr[1:], how='outer')
    merged_df.fillna(0, inplace=True)
    return merged_df