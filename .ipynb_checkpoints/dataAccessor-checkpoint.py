# import requests
# import io
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
# import pandas as pd

def get_intraday(ticker):
    yf.pdr_override()
    raise NotImplementedError('TODO')
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={av_api_key}&datatype=csv&outputsize=full'
    # urlData = requests.get(url).content

    # df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    # df['ticker'] = ticker
    # df['timestamp'] = pd.to_datetime(df['timestamp'])
    # df.sort_values(by=['timestamp'], ascending=True, inplace=True)
    # return df 

def get_daily(ticker, start_date = None, end_date = None):
    yf.pdr_override()
    df = pdr.get_data_yahoo(ticker)
    
    df.reset_index(inplace=True)
    df.rename(
        columns={
            'Date':'date',
            'Open':'open',
            'Close':'close',
            'High':'high',
            'Low':'low',
            'Adj Close':'adj_close'
            ,'Volume':'volume'
        },
        inplace=True
    )
    df['ticker'] = ticker
    df['date'] = pd.to_datetime(df['date'])

    if start_date != None:
        df = df.loc[df.date >= pd.to_datetime(start_date)]
    if end_date != None:
        df = df.loc[df.date <= pd.to_datetime(end_date)]
    
    df.sort_values(by=['date'], ascending=True, inplace=True)
    return df

def get_singletime(ticker,date,dot,price_freq):
    
    if price_freq == 'daily':
        prices = get_daily(ticker)
        prices = prices.loc[prices.date == date]

        prices = prices[['ticker','date',dot]]
        prices.rename(columns={dot:'price'},inplace=True)

    elif price_freq == 'intraday':
        # prices = get_intraday(ticker,av_api_key)
        # prices = prices.loc[prices.timestamp == date]

        # prices = prices[['ticker','timestamp',dot]]
        raise NotImplementedError('TODO')

    return prices