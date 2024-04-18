#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /states_list
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ route to /states_list """
    states_obj = storage.all(State)
    return render_template('7-states_list.html', states=states_obj)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occured: {}".format(exception))
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
