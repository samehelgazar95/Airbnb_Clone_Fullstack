#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /hbnb_filters
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ route to / """
    return "Hello HBNB!"


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ route to /hbnb_filters """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occurred: {}".format(exception))
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
