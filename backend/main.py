from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    try:
        static_dir = '/app/frontend/dist'
        app.logger.info(f'Serving path: {path}')
        app.logger.info(f'Static dir contents: {os.listdir(static_dir)}')
        
        if path and os.path.exists(os.path.join(static_dir, path)):
            return send_from_directory(static_dir, path)
        return send_from_directory(static_dir, 'index.html')
    except Exception as e:
        app.logger.error(f'Error serving path {path}: {str(e)}')
        raise

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.logger.info(f'Starting server on port {port}')
    app.run(host='0.0.0.0', port=port)