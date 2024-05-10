import os

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

from controllers.routes import *

api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True)