import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

def get_intraday(ticker):
    yf.pdr_override()
    raise NotImplementedError('TODO')

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
        
        raise NotImplementedError('TODO')

    return prices