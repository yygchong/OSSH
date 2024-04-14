# flaskr/__init__.py
"""
Factory method
"""

import os

from flask import Flask
import requests
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from . import establish_connection, db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the regular instance configurations
        app.config.from_pyfile('config.py', silent=True)
        pass
    else:
        # load the testing configurations
        pass

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def show_dashboard():
        """This is a view function for displaying the dashboard and
        metrics of what devices are connected and their statuses. 
        Used for debugging and manual set up of devices."""

        return render_template('dashboard.html')

    @app.route("/device_management")
    def device_management():
        """This is a view function for establishing a connection with
        our IOT device(s). This is used for debugging and manual set up of devices."""

        sync_status = establish_connection.establish_connection()

        return f"Device status: {sync_status}"
        
    db.init_app(app)
    
    return app