from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__, static_folder='/app/frontend/dist', static_url_path='')
CORS(app)

stored_address = '3250 clarendon rd. Cleveland Heights Ohio 44118'

@app.route('/api/address', methods=['GET'])
def get_address():
    return jsonify({'address': stored_address})

@app.route('/api/address', methods=['POST'])
def update_address():
    global stored_address
    data = request.json
    if 'address' in data:
        stored_address = data['address']
        return jsonify({'success': True, 'address': stored_address})
    return jsonify({'success': False, 'error': 'No Address Provided'}), 400

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)