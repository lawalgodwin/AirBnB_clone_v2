#!/usr/bin/python3

"""A script that starts a flask web app at port 5000
on the host=0.0.0.0
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def handle_index():
    """Handle request to the index route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def handle_hbnb():
    """Serve request to the hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def handle_cText(text):
    """Handle request to /c/{variable}"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def handle_pythonText(text='is cool'):
    """Handle request to the python/text route"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
