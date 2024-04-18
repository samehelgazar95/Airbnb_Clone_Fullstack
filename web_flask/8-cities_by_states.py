#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /cities_by_states
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ route to /cities_by_states """
    states_obj = storage.all(State)
    return render_template('8-cities_by_states.html', states=states_obj)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occured: {}".format(exception))
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
