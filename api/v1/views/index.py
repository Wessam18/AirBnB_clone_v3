#!/usr/bin/python3
""" import modules"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """Route to return the status of the API"""
    return jsonify({"status": "OK"})
