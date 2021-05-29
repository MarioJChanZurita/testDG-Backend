from flask import Flask
from .extensions import mongo
from .routes import page

app = Flask(__name__)


def initApp(config):
    app.config.from_object(config)
    app.register_blueprint(page)

    mongo.init_app(app)

    return app
