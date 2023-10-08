import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


os.getenv('ENV', 'd')

ALPHA_VANTAGE_API_KEY = os.getenv('ENV', 'ALPHA_API_KEY')

def get_historical_stock_data(symbol, interval='daily'):
    print("Coming here")
    endpoint = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY' if interval == 'intraday' else 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'interval': '1min' if interval == 'intraday' else '1d',
        'apikey': ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if 'Time Series (1min)' in data:
        # For intraday data
        stock_data = data['Time Series (1min)']
    elif 'Time Series (Daily)' in data:
        # For daily data
        stock_data = data['Time Series (Daily)']
    else:
        return None

    return stock_data
