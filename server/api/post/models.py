from sanic_openapi import doc

class PostInputModel:
    name = doc.String('청원 제목', required=True)
    content = doc.String('청원 내용', required=True)
    image = doc.String('이미지 URL')
