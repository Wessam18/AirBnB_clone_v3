#!/usr/bin/python3
""" import modules"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    """Route to return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_count():
    """Endpoint to retrieve the number of each object type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    return jsonify(stats)
