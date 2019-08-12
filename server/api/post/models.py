from sanic_openapi import doc

class PostInputModel:
    name = doc.String('청원 제목', required=True)
    content = doc.String('청원 내용', required=True)
    image = doc.String('이미지 URL')
    topic = doc.String('분류')

class PostEditModel:
    name = doc.String('청원 제목')
    content = doc.String('청원 내용')
    image = doc.String('이미지 URL')
    topic = doc.String('분류')

class PostCreatedModel:
    post_id = doc.String('생성된 포스트 id')

class PostCommentModel:
    content = doc.String('댓글 내용')
    timestamp = doc.Integer('타임스탬프')
    author = doc.Integer('게시자의 디미고인 id')
    author_id = doc.Integer('게시자의 ObjectId')

class PostViewModel:
    name = doc.String('포스트 제목')
    content = doc.String('포스트 본문')
    likes = doc.Integer('댓글 수')
    comments = doc.List(PostCommentModel, '청원 댓글')
    image = doc.String('포스트 이미지')
    timestamp = doc.Integer('타임스탬프')
    author = doc.Integer('게시자의 디미고인 id')
    author_id = doc.Integer('게시자의 ObjectId')
    topic = doc.String('분류')
