from sanic import Blueprint
from server.api.auth import auth_api
from server.api.post import post_api

api = Blueprint.group(
    auth_api,
    post_api
)
