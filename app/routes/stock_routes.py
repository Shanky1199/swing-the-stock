from flask import Blueprint, request, jsonify
from controllers.stock_controller import get_stock_details_controller

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/api/stocks', methods=['POST'])
def add_stock():
    try:
        data = request.get_json()
        # Extract data from request
        # ...
        
        # Call the service function to add stock
        stock, error_message = StockService.add_stock(data)

        if stock:
            return jsonify({"message": "Stock added successfully"}), 201
        else:
            return jsonify({"message": error_message}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


stock_bp.route('/api/stock-details', methods=['GET'])
def get_stock():
    try:
        symbol = request.args.get('symbol')
        date = request.args.get('date')

        if not symbol or not date:
            return jsonify({"error": "Symbol and date parameters are required."}), 400

        stock_details = get_stock_details_controller(symbol, date)

        if stock_details:
            return jsonify(stock_details), 200
        else:
            return jsonify({"message": "No data found for the given symbol and date."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@stock_bp.route('/api/stocks', methods=['GET'])
def get_all_stocks():
    try:
        # Call the service function to get all stocks
        stocks = StockService.get_all_stocks()

        # Convert list of stock objects to JSON and return
        return jsonify({"stocks": [stock.serialize() for stock in stocks]}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
