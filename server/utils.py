from sanic.exceptions import abort
import jwt

def jwt_required(function):
    def wrap_function(*args, **kwargs):
        request = args[0]
        token = request.headers.get('authorization') or request.args.get('token')
        if not token:
            abort(401)

        identity = jwt.decode(token, verify=False)['data']
        return function(*args, identity, **kwargs)
    return wrap_function
