#!/usr/bin/python3
"""A script that starts a flask web app at port 5000
on host=0.0.0.0
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Handler for home page request"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_handler():
    """Handler for request to hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.debug = None
    app.run(host='0.0.0.0', port=5000)
