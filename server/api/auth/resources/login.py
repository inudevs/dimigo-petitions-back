from server.api.auth import auth_api
from server.api.auth.models import LoginModel, token_model
from server.api.auth.utils.dimigoin import dimigo_auth, dimigo_profile
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from sanic_jwt_extended import create_access_token, create_refresh_token

@auth_api.post('/login')
@doc.summary('검증 후 사용자 토큰 생성(로그인)')
@doc.consumes(LoginModel, content_type='application/json', location='body')
@doc.produces(token_model, content_type='application/json', description='성공적')
@doc.response(403, None, description='잘못된 로그인 정보')
@doc.response(404, None, description='디미고인 API 서버 오류')
@doc.response(500, None, description='새로운 사용자 DB에 저장 중 오류')
async def AuthLogin(request):
    _id, _password = request.json['id'], request.json['password']

    dimigoin_token = await dimigo_auth(_id, _password)
    if not dimigoin_token: # 잘못된 로그인
        abort(404)

    user = await request.app.db.users.find_one({
        'id': _id
    })  # check if _id exists in DB
    if not user:
        # if not, query student profile and save to DB
        student = await dimigo_profile(dimigoin_token)
        if not student: # API server error
            abort(403)
        user = {
            'id': _id,
            'student': student
        }
        res = await request.app.db.users.insert_one(user)
        if not res.acknowledged:
            abort(500)

    token = await create_access_token(identity=_id, app=request.app)
    refresh_token = await create_refresh_token(identity=_id, app=request.app)
    return res_json({
        'token': token,
        'refresh_token': refresh_token,
        'user': user['student']
    })
