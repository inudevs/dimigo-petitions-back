from server.api.comments import comment_api
from sanic.views import HTTPMethodView
from sanic.exceptions import abort
from sanic.response import json as res_json
from sanic_openapi import doc
from server.utils import jwt_required
from sanic_jwt_extended.tokens import Token
from bson import ObjectId
import time


@comment_api.post('/<post_id>')
@jwt_required
@doc.summary('청원 댓글 생성')
async def write_comments(request, identity: dict, post_id):
    post = await request.app.db.posts.find_one(ObjectId(post_id))
    if not post:
        abort(404)

    if any(comment['author_id'] == identity['id'] for comment in post['comments']):
        abort(400)

    comment = {
        'content': request.json['content'],
        'timestamp': int(time.time()),
        'author': '{} {}'.format(identity['student']['serial'], identity['name']),
        'author_id': identity['id'],
    }

    res = await request.app.db.posts.update_one({'_id': ObjectId(post_id)}, {
        '$push': {
            'comments': comment
        }
    })
    if not res.acknowledged:
        abort(500)

    return res_json({})


@comment_api.put('/<post_id>')
@jwt_required
@doc.summary('청원 댓글 수정')
async def edit_comments(request, identity: dict, post_id):
    res = await request.app.db.posts.update_one({
        '_id': ObjectId(post_id),
        'comments.author_id': identity['id']
    }, {
        '$set': {
            'comments.$.content': request.json['content']
        }
    })
    if not res.acknowledged:
        abort(404)
    return res_json({})


@comment_api.delete('/<post_id>')
@jwt_required
@doc.summary('청원 댓글 삭제')
async def delete_comments(request, identity: dict, post_id):
    res = await request.app.db.posts.update_one({'_id': ObjectId(post_id)}, {
        '$pull': {
            'comments': {
                'author_id': identity['id'] 
            }
        }
    })
    if not res.acknowledged:
        abort(404)
    return res_json({})
