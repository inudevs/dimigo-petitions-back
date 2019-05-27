from sanic_openapi import doc

class LoginModel:
    id = doc.String('디미고 아이디', required=True)
    password = doc.String('디미고 패스워드', required=True)

user_model = {
    'idx': int,
    'name': str,
    'grade': str,
    'klass': str,
    'number': str,
    'serial': str,
    'photo': str,
    'email': str,
    'user_type': str
}

token_model = {
    'token': str,
    'refresh_token': str,
    'user': user_model
}
