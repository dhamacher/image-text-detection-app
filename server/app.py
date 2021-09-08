import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from src.ml.model import get_text_from_image

import datetime as dt
import json

error_response = { 'status': 'ERROR', 'exception': None }
DEBUG = os.getenv('FLASK_DEBUG')
ENV = os.getenv('APP_ENV')

# Create the application.
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/health-check', methods=['GET'])
def health_check():
    try:
        json_raw = {
            'status': 'alive - ready to accept requests',
            'time': str(dt.datetime.now()),
            'metadata': 'Image to Text Detection App'
        }
        json_payload = json.dumps(json_raw)
        return jsonify(json_payload)
    except Exception as e:
        print(str(e))
        raise(e)


@app.route('/getText', methods=['POST'])
def get_text():
    try:
        if request.method == "POST":
            file_obj = request.files.get('file')
            result = get_text_from_image(file_obj)
            return jsonify(result)
        else:
            error_response['exception'] = 'Non POST request not valid!'
            return jsonify(error_response)
    except Exception as e:
        print(str(e))
        raise(e)


if __name__ == '__main__':
    app.run()
