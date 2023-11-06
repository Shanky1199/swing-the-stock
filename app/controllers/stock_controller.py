from services.stock_service import get_stock_details

def get_stock_details_controller(symbol, date_str):
    try:
        stock_details = get_stock_details(symbol, date_str)
        return stock_details
    except Exception as e:
        # Handle exceptions if necessary
        raise e
