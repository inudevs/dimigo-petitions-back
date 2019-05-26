from sanic import Blueprint

auth_api = Blueprint('auth', url_prefix='/auth')

__import__('server.api.auth.resources.login')
