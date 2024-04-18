#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /states
- Create route to /states/<id>
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ route to / """
    return "Hello HBNB!"


@app.route('/states', strict_slashes=False)
def states():
    """ route to /states """
    states_obj = storage.all(State)
    return render_template('7-states_list.html', states=states_obj)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ route to /states/<id> """
    states_obj = storage.all(State)
    for state in states_obj.values():
        if state.id == id:
            state_obj = state
            break
        else:
            state_obj = None
    return render_template('9-states.html', state=state_obj)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occured: {}".format(exception))
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
