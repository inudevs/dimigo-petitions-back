from server.api.post import post_api
from server.api.post.models import PostInputModel
from sanic.views import HTTPMethodView
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from sanic_jwt_extended import jwt_required
from sanic_jwt_extended.tokens import Token
from bson import ObjectId
import time

@post_api.post('/')
@jwt_required
@doc.summary('청원 생성')
@doc.consumes(PostInputModel, content_type='application/json', location='body')
async def write_post(request, token: Token):
    user = token.jwt_identity
    post = {
        'name': request.json['name'],
        'content': request.json['content'],
        'likes': [],
        'image': request.json.get('image'),
        'timestamp': int(time.time()),
        'author': user['name'],
        'author_id': user['id']
    }
    res = await request.app.db.posts.insert_one(post)
    if not res.acknowledged:
        abort(500)
    return res_json({
        'post_id': str(res.inserted_id)
    })

@post_api.get('/<post_id>')
@jwt_required
@doc.summary('청원 보기')
async def view_post(request, token: Token, post_id):
    post = await request.app.db.posts.find_one(ObjectId(post_id))
    if not post:
        abort(404)
    post['_id'] = str(post['_id'])
    return res_json(post)

@post_api.put('/<post_id>')
@jwt_required
@doc.summary('청원 수정')
async def edit_post(request, token: Token, post_id):
    post = await request.app.db.posts.find_one(ObjectId(post_id))
    if not post:
        abort(404)
    _name = request.json.get('name')
    _content = request.json.get('content')
    _image = request.json.get('image')
    res = await request.app.db.posts.update_one({'_id': ObjectId(post_id)}, {
        '$set': {
            'name': _name if _name else post['name'],
            'content': _name if _content else post['content'],
            'image': _name if _image else post['image'],
        }
    })
    if not res.acknowledged:
        abort(500)
    return res_json({})

@post_api.delete('/<post_id>')
@jwt_required
@doc.summary('청원 삭제')
async def delete_post(request, token: Token, post_id):
    res = await request.app.db.posts.delete_one({'_id': ObjectId(post_id)})
    if not res.acknowledged:
        abort(404)
    return res_json({})
