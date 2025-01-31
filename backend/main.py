from flask import Flask, request, jsonify
from flask_cors import CORS
# from app.services.price_optimizer import PriceOptimizer
# from app.scrapers.base_scraper import StoreScraper

app = Flask(__name__)
CORS(app)

#price_optimizer = PriceOptimizer()

# @app.route('/api/stores', methods=['GET'])
# def get_stores():
#     """Get list of stores near location"""
#     lat = request.args.get('lat')
#     lng = request.args.get('lng')
#     return jsonify(price_optimizer.get_nearby_stores(lat, lng))

# @app.route('/api/search', methods=['POST'])
# def search_prices():
#     """Search prices for grocery items"""
#     data = request.get_json()
#     items = data.get('items', [])
#     stores = data.get('stores', [])
#     return jsonify(price_optimizer.get_optimal_lists(items, stores))

# @app.route('/api/save-list', methods=['POST'])
# def save_list():
#     """Save a grocery list"""
#     data = request.get_json()
#     return jsonify({"id": price_optimizer.save_list(data)})

if __name__ == '__main__':
    app.run(debug=True)