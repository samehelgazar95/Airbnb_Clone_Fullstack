#!/usr/bin/python3
"""
Initiate Flask
- Create route to /
- Create route to hbnb /hbnb
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Creating the home route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Creating the hbnb route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
