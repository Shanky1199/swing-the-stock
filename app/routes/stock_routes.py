from flask import Blueprint, request, jsonify
from services.stock_service import StockService

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

@stock_bp.route('/api/stocks/<int:stock_id>', methods=['GET'])
def get_stock(stock_id):
    try:
        # Call the service function to get stock by ID
        stock = StockService.get_stock_by_id(stock_id)

        if stock:
            # Convert stock object to JSON and return
            return jsonify({"stock": stock.serialize()}), 200
        else:
            return jsonify({"message": "Stock not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@stock_bp.route('/api/stocks', methods=['GET'])
def get_all_stocks():
    try:
        # Call the service function to get all stocks
        stocks = StockService.get_all_stocks()

        # Convert list of stock objects to JSON and return
        return jsonify({"stocks": [stock.serialize() for stock in stocks]}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
