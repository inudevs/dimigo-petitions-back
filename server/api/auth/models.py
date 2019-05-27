from sanic_openapi import doc

class LoginModel:
    id = doc.String('디미고 아이디', required=True)
    password = doc.String('디미고 패스워드', required=True)

class UserModel:
    idx = doc.Integer('디미고인에서의 idx')
    name = doc.String('이름')
    grade = doc.String('학년')
    klass = doc.String('반')
    number = doc.String('번호')
    serial = doc.String('학번')
    photo = doc.String('프로필 사진')
    email = doc.String('이메일')
    user_type = doc.String('회원 종류')

class TokenModel:
    token = doc.String('JWT 토큰')
    refresh_token = doc.String()
    user = UserModel
