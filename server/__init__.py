from sanic import Sanic, Blueprint
from sanic_openapi import swagger_blueprint, doc
from sanic_cors import CORS
from config import DevConfig

def create_app():
    _app = Sanic(__name__)
    _app.config.from_object(DevConfig)
    CORS(_app)
    return _app


app = create_app()
app.blueprint(swagger_blueprint)

from server.api import api
app.blueprint(api)
