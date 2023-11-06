from models import Stock
from datetime import datetime

def get_stock_details(symbol, date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        stock_details = Stock.query.filter_by(symbol=symbol, date=date).first()
        if stock_details:
            return format_stock_details(stock_details)
        else:
            return None
    except Exception as e:
        # Handle exceptions if necessary
        raise e

def format_stock_details(stock_details):
    return {
        "symbol": stock_details.symbol,
        "date": stock_details.date.strftime('%Y-%m-%d'),
        "open_price": stock_details.open_price,
        "high_price": stock_details.high_price,
        "low_price": stock_details.low_price,
        "close_price": stock_details.close_price,
        "volume": stock_details.volume
    }
