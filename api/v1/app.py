#!/usr/bin/python3
""" import modules"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tearsdown(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """handle error 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """Starts the Flask web server"""
    from api.v1.views import *
    Host1 = getenv('HBNB_API_HOST', '0.0.0.0')
    Port1 = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=Host1, port=Port1, threaded=True)
