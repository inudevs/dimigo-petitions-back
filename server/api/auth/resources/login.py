from server.api.auth import auth_api
from server.api.auth.models import login_model
from sanic.response import json as res_json
from sanic_openapi import doc

@auth_api.route('/login')
@doc.summary('검증 후 사용자 토큰 생성(로그인)')
@doc.produces(login_model)
async def auth_login(request):
    return res_json({
        'token': '',
        'refresh_token': ''
    })
