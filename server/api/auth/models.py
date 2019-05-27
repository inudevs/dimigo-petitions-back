from sanic_openapi import doc

class LoginModel:
    id = doc.String('디미고 아이디', required=True)
    password = doc.String('디미고 패스워드', required=True)

class UserModel:
    idx = doc.Integer()
    name = doc.String()
    grade = doc.String()
    klass = doc.String()
    number = doc.String()
    serial = doc.String()
    photo = doc.String()
    email = doc.String()
    user_type = doc.String()

class TokenModel:
    token = doc.String()
    refresh_token = doc.String()
    user = UserModel
