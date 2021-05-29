from flask import Flask
from flask.wrappers import Response
from bson import json_util

from .extensions import mongo

app = Flask(__name__)

apiRoute = '/api'
salesRoute = '/sellers'


@app.route('/')
def index():

    return 'Oh no, estoy vivo :c'


@app.route(apiRoute + salesRoute, methods=['GET'])
def getSellers():
    users = mongo.db.seller.find()
    response = json_util.dumps(users)

    return response


def initApp(config):
    app.config.from_object(config)

    mongo.init_app(app)

    return app
