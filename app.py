from flask import Flask, render_template, jsonify, request
import face_recognition
from werkzeug.utils import secure_filename

import image
import requests

app = Flask(__name__)


# ('/api/v1/hello')

@app.route('/api/v1/hello', methods=['GET'])
def api_hello():
    file = request.files['image']
#    filename = secure_filename(file.filename)
    data = {'message': image.check_image(file)}
    return jsonify(data)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
