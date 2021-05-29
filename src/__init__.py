from flask import Flask, request
from bson import json_util

from .extensions import mongo

app = Flask(__name__)

apiRoute = '/api'
salesRoute = '/sellers'
clientRoute = '/clients'


@app.route('/')
def index():

    return 'Oh no, estoy vivo :c'


@app.route(apiRoute + salesRoute, methods=['GET'])
def getSellers():
    users = mongo.db.seller.find()
    response = json_util.dumps(users)

    return response


@app.route(apiRoute + salesRoute, methods=['PUT'])
def insertSellers():
    content = request.get_json()
    for seller in content:
        mongo.db.seller.insert_one(
            {
                "code": seller["code"],
                "first_name": seller["first_name"],
                "last_name": seller["last_name"]
            }
        )

    return 'test'


def initApp(config):
    app.config.from_object(config)

    mongo.init_app(app)

    return app
