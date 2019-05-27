from server.api.post import post_api
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from sanic_jwt_extended import jwt_required

@post_api.post('/write')
@jwt_required
@doc.summary('청원 작성')
async def PostWrite(request):
    return res_json({})
