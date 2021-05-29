from bson import ObjectId, json_util
from flask import request, jsonify, Response, Blueprint, make_response

from .extensions import mongo

page = Blueprint('clients', __name__)

apiRoute = '/api'
salesRoute = '/sellers'
clientRoute = '/clients'


@page.route(apiRoute + clientRoute, methods=['PUT'])
def create():
    content = request.get_json()
    for client in content:
        mongo.db["client"].insert_one(
            {
                "code": client["code"],
                "first_name": client["first_name"],
                "last_name": client["last_name"]
            }
        )

    return make_response({"message": "success"}, 200)


@page.route(apiRoute + clientRoute + '/<client_id>', methods=['PUT'])
def update(client_id):
    code = request.json['code']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    if code and first_name and last_name:
        client_id = mongo.db["client"].update_one({
            '_id': ObjectId(client_id['$oid']) if '$oid' in client_id else ObjectId(client_id)},
            {'$set': {
                'code': code,
                'first_name': first_name,
                'last_name': last_name,
            }})
        response = jsonify(
            {'message': 'Client' + client_id + 'updated successfully'})
        response.status_code = 200
    return response


@page.route(apiRoute + clientRoute + '/<client_id>', methods=['DELETE'])
def delete_movie(client_id):
    mongo.db["client"].delete_one({'id': ObjectId(client_id)})
    response = jsonify(
        {'message': 'Client' + client_id + 'deleted successfully'})
    response.status_code = 200
    return response


@page.route(apiRoute + clientRoute + '/<client_id>', methods=['GET'])
def get(client_id):
    client = mongo.db["client"].find_one({'_id': ObjectId(client_id), })
    response = json_util.dumps(client)
    return Response(response, mimetype="application/json")


@page.route(apiRoute + clientRoute + '/all', methods=['GET'])
def get_all():
    client = mongo.db["client"].find()
    response = json_util.dumps(client)
    return response


@page.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@page.route('/')
def index():

    return 'Oh no, estoy vivo :c'


@page.route(apiRoute + salesRoute, methods=['GET'])
def getSellers():
    users = mongo.db.seller.find()
    response = json_util.dumps(users)

    return response


@page.route(apiRoute + salesRoute, methods=['PUT'])
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

    return make_response({"message": "success"}, 200)


@page.route(apiRoute + salesRoute + '/<id>', methods=['GET'])
def getUserById(id):
    user = mongo.db.seller.find_one(
        {
            'code': str(id)
        }
    )
    response = json_util.dumps(user)

    return response
