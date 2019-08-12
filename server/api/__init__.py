from sanic import Blueprint
from server.api.auth import auth_api
from server.api.posts import post_api
from server.api.comments import comment_api

api = Blueprint.group(
    auth_api,
    post_api,
    comment_api
)
