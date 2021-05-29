from flask import Flask

from .extensions import mongo

app = Flask(__name__)


@app.route('/')
def index():

    return 'Oh no, estoy vivo :c'


def initApp(config):
    app.config.from_object(config)

    mongo.init_app(app)

    return app
