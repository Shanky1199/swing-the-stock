from flask import Blueprint, request, jsonify
from services.watchlist_service import WatchlistService

watchlist_bp = Blueprint('watchlist', __name__)

@watchlist_bp.route('/api/watchlist/<int:user_id>', methods=['GET', 'POST', 'DELETE'])
def watchlist_operations(user_id):
    if request.method == 'GET':
        # View user's watchlist
