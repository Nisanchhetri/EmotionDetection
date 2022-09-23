from flask import Flask, jsonify, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from routes.api_route import create_route
from settings import shared_components

import sys
import os


def init_app():

    app = Flask(__name__)
    app = create_route(app)
    # Load Config file for Database
    app.config.from_pyfile('configs/config.cfg')
    CORS(app)
    mongo = PyMongo(app)

    #Selecting database
    db = mongo.db

    shared_components['db'] = db

    return app

app = init_app()

@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = "This route is currently not supported."
    

    # Sending OK response
    # Returning the object
    return Response(message, status=404)