from server.api.post import post_api
from sanic.views import HTTPMethodView
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from sanic_jwt_extended import jwt_required

class PostView(HTTPMethodView):
    @jwt_required
    @doc.summary('청원 보기')
    async def get(self, request):
        return res_json({})

    @jwt_required
    @doc.summary('청원 생성')
    async def post(self, request):
        return res_json({})

    @jwt_required
    @doc.summary('청원 수정')
    async def put(self, request):
        return res_json({})

    @jwt_required
    @doc.summary('청원 삭제')
    async def delete(self, request):
        return res_json({})

post_api.add_route(PostView.as_view(), '/')
