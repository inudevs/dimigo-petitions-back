from sanic import Blueprint

post_api = Blueprint(
    'post',
    url_prefix='/post',
    strict_slashes=True
)

__import__('server.api.post.resources.post')
