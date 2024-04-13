# flaskr/__init__.py
"""
Factory method
"""

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
        
    # )

    if test_config is None:
        # load the regular instance configurations
        pass
    else:
        # load the testing configurations
        pass

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hey I'm Open Source Smart Home, but you can call me OSSH for short. I am here to help you automate your home and IOT devices on your local area network to allow for more customizability, quicker action times, and more privacy from big tech smart home devices."

    return app