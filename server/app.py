from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
from src.utils.files import save_image
from src.ml.model import get_text_from_image
import datetime as dt
import json
from pathlib import Path

error_response = { 'status': 'ERROR', 'exception': None }

# configuration
DEBUG = True
ENV = 'DEV'

_pwd = Path().cwd()
sys.path.append(_pwd)






# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/health-check', methods=['GET'])
def health_check():
    json_raw = {
        'status': 'alive - ready to accept requests',
        'time': str(dt.datetime.now()),
        'metadata': 'Image to Text Detection App'
    }
    json_payload = json.dumps(json_raw)
    return jsonify(json_payload)


@app.route('/submitImage', methods=['POST'])
def fetch_image():
    # TODO: Build package with utility functions for this.
    if request.method == "POST":
        file_obj = request.files.get('file')
        save_image(file_obj)
    return jsonify('Nothing Happened!')


@app.route('/getText', methods=['POST'])
def get_text():
    # TODO: Build package with utility functions for this.
    if request.method == "POST":
        file_obj = request.files.get('file')
        result = get_text_from_image(file_obj)
        return jsonify(result)
    else:
        error_response['exception'] = 'Non POST request not valid!'
        return jsonify(error_response)




if __name__ == '__main__':
    # TODO: Maintain a stateless app where storing of data is not neccessary.
    app.run()