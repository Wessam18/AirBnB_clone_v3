#!/usr/bin/python3
""" import modules"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Route to return the status of the API"""
    result = {"status": "OK"}
    return jsonify(result)


@app_views.route('/stats', strict_slashes=False)
def get_count():
    """Endpoint to retrieve the number of each object type"""
    stats = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(stats)
