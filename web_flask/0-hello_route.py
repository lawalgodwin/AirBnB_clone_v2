#!/usr/bin/python3

"""A flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Say hello to the world"""

    return ("Hello HBNB!")


if __name__ == '__main__':
    app.debug = None
    app.run(host='0.0.0.0', port=5000)
