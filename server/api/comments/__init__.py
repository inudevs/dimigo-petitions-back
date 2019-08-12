from sanic import Blueprint

comment_api = Blueprint(
    'Comments',
    url_prefix='/comments',
    strict_slashes=True
)

__import__('server.api.comments.resources.comments')
