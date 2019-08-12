from sanic import Blueprint

auth_api = Blueprint(
    'Auth',
    url_prefix='/auth',
    strict_slashes=True
)

__import__('server.api.auth.resources.login')
