import requests
import io
import pandas as pd

def get_intraday(ticker,av_api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={av_api_key}&datatype=csv&outputsize=full'
    urlData = requests.get(url).content

    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return df 

def get_daily(ticker,av_api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={av_api_key}&datatype=csv&outputsize=full'
    urlData = requests.get(url).content

    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return df