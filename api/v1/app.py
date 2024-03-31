#!/usr/bin/python3
""" """

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv



app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    Host1 = getenv('HBNB_API_HOST', '0.0.0.0')
    Port1 = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=Host1, port=Port1, threaded=True)
    