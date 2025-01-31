from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='/app/frontend/dist', static_url_path='')
CORS(app)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def root():
    return app.send_static_file('index.html')