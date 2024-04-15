#!/usr/bin/python3
"""
Create v1 app
"""
from os import getenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)

@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    storage.close()

@app.errorhandler(404)
def not_found(e):
    """Not found handle"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """
    Main Entrypoint
    """
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(debug=True, host=host, port=port, threaded=True)
