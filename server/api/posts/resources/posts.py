from server.api.posts import post_api
from server.api.posts.models import (
    PostInputModel, 
    PostEditModel,
    PostCreatedModel,
    PostViewModel
)
from sanic.views import HTTPMethodView
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from server.utils import jwt_required
from sanic_jwt_extended.tokens import Token
from bson import ObjectId
import time

@post_api.get('/')
@jwt_required
@doc.summary('청원 리스트')
async def list_post(request, identity: dict):
    cursor = request.app.db.posts.find({})
    posts = await cursor.to_list(length=50)
    for idx, post in enumerate(posts):
        post['id'] = str(post['_id'])
        del post['_id']
        post['idx'] = idx + 1
        post['likes'] = len(post['comments'])
        post['expire'] = '2019-09-15' # test data
    return res_json({ 'posts': posts })

@post_api.post('/')
@jwt_required
@doc.summary('청원 생성')
@doc.consumes(PostInputModel, content_type='application/json', location='body')
@doc.produces(PostCreatedModel, content_type='application/json', description='성공적')
@doc.response(200, None, description='성공')
@doc.response(500, None, description='저장 중 오류')
async def write_post(request, identity: dict):
    post = {
        'name': request.json['name'],
        'content': request.json['content'],
        'comments': [],
        'image': request.json.get('image'),
        'timestamp': int(time.time()),
        'author': identity['name'][0] + '**',
        'author_id': identity['id'],
        'topic': request.json['topic']
    }
    res = await request.app.db.posts.insert_one(post)
    if not res.acknowledged:
        abort(500)
    return res_json({
        'post_id': str(res.inserted_id)
    })

@post_api.get('/<post_id:string>')
# @jwt_required
@doc.summary('청원 보기')
@doc.produces(PostViewModel, content_type='application/json', description='성공적')
@doc.response(200, None, description='성공')
@doc.response(404, None, description='잘못된 요청; 없는 포스트')
async def view_post(request, post_id):
    post = await request.app.db.posts.find_one(ObjectId(post_id))
    if not post:
        abort(404)
    post['_id'] = str(post['_id'])

    # TODO: post metadata
    post['status'] = True
    post['start'] = '2019-08-12'
    post['expire'] = '2019-09-15'

    post['likes'] = len(post['comments'])
    return res_json(post)

@post_api.put('/<post_id>')
@jwt_required
@doc.summary('청원 수정')
@doc.consumes(PostEditModel, content_type='application/json', location='body')
@doc.response(200, None, description='성공')
@doc.response(404, None, description='잘못된 요청; 없는 포스트')
@doc.response(404, None, description='수정 중 오류')
async def edit_post(request, identity: dict, post_id):
    post = await request.app.db.posts.find_one(ObjectId(post_id))
    if not post:
        abort(404)
    _name = request.json.get('name')
    _content = request.json.get('content')
    _image = request.json.get('image')
    _topic = request.json.get('topic')
    res = await request.app.db.posts.update_one({'_id': ObjectId(post_id)}, {
        '$set': {
            'name': _name if _name else post['name'],
            'content': _name if _content else post['content'],
            'image': _name if _image else post['image'],
            'topic': _topic if _topic else post['topic']
        }
    })
    if not res.acknowledged:
        abort(500)
    return res_json({})

@post_api.delete('/<post_id>')
@jwt_required
@doc.summary('청원 삭제')
@doc.response(200, None, description='성공')
@doc.response(404, None, description='잘못된 요청; 없는 포스트')
async def delete_post(request, identity: dict, post_id):
    res = await request.app.db.posts.delete_one({'_id': ObjectId(post_id)})
    if not res.acknowledged:
        abort(404)
    return res_json({})
