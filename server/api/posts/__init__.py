from sanic import Blueprint

post_api = Blueprint(
    'Posts',
    url_prefix='/posts',
    strict_slashes=True
)

__import__('server.api.posts.resources.posts')
