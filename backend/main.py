from flask import Flask, request, jsonify
from flask_cors import CORS
import googlemaps
from datetime import datetime


app = Flask(__name__, static_folder='/app/frontend/dist', static_url_path='')
CORS(app)

# stored variables
stored_address = '3250 Clarendon rd. Cleveland Heights Ohio 44118'
myKey = 'AIzaSyDnNPD1pEn4CeGHdqMtFTLaWgeVLqqCMzc'


gmaps = googlemaps.Client(key=myKey)

@app.route('/api/address', methods=['GET'])
def get_address():
    return jsonify({'address': stored_address})

@app.route('/api/address', methods=['POST'])
def update_address():
    global stored_address
    data = request.json
    if 'address' in data:
        stored_address = data['address']
        dict_address = gmaps.geocode(address=stored_address)
        lat_lng_dict = dict_address[0].get("geometry").get("location")
        results = gmaps.places(query='Grocery', location=lat_lng_dict, radius = 5000)
        return jsonify({'success': True, 'address': lat_lng_dict, 'stores': results})
    return jsonify({'success': False, 'error': 'No Address Provided'}), 400




@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)