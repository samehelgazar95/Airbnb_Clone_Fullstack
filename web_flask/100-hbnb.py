#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /hbnb
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ route to / """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route to /hbnb """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occurred: {}".format(exception))
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
