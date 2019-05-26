from sanic import Blueprint
from server.api.auth import auth_api

api = Blueprint.group(
    auth_api
)
