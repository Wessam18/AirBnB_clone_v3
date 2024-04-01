#!/usr/bin/python3
""" import modules"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


from api.v1.views import *

if __name__ == "__main__":
    """Starts the Flask web server"""
    Host1 = getenv('HBNB_API_HOST', '0.0.0.0')
    Port1 = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=Host1, port=Port1, threaded=True, debug=True)
