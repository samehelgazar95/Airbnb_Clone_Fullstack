#!/usr/bin/python3
"""
Initiate Flask
- Create route to /
- Create route to hbnb /hbnb
- Create route to /c/<text>
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ route to home """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route to hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_url(text):
    """ route to /c/<text> """
    text_val = text.replace('_', ' ')
    return "C {}".format(text_val)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
