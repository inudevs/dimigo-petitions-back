from server.api.auth import auth_api
from server.api.auth.models import login_model
from sanic.response import json as res_json
from sanic_openapi import doc
from sanic_jwt_extended import create_access_token, create_refresh_token

@auth_api.route('/login')
@doc.summary('검증 후 사용자 토큰 생성(로그인)')
@doc.produces(login_model)
async def auth_login(request):
    token = await create_access_token(identity='test', app=request.app)
    refresh_token = await create_refresh_token(identity='test', app=request.app)
    return res_json({
        'token': token,
        'refresh_token': refresh_token
    })
