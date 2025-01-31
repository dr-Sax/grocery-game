from flask import Flask, send_from_directory, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
    return 'OK'

@app.route('/')
def root():
    return send_file('/app/frontend/dist/index.html')

@app.route('/<path:path>')
def assets(path):
    return send_from_directory('/app/frontend/dist', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))