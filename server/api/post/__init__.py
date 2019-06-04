from sanic import Blueprint

post_api = Blueprint(
    'posts',
    url_prefix='/posts',
    strict_slashes=True
)

__import__('server.api.post.resources.posts')
__import__('server.api.post.resources.likes')
