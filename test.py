import os, sys, json
import pytest
from server import create_app
import logging

LOGGER = logging.getLogger(__name__)
def custom_log(text):
    LOGGER.info('-' * 20 + ' {} '.format(text) + '-' * 20)

@pytest.yield_fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))

@pytest.yield_fixture
def user():
    with open(os.path.join(sys.path[0], 'secret.json')) as secret_file:
        user = json.load(secret_file)
    yield user

@pytest.yield_fixture
async def token(test_cli, user):
    with open(os.path.join(sys.path[0], 'secret.json')) as secret_file:
        user = json.load(secret_file)
    resp = await test_cli.post('/auth/login', json=user)
    resp_json = await resp.json()
    yield resp_json['token']

async def test_fixture_login(test_cli, user):
    resp = await test_cli.post('/auth/login', json=user)
    assert resp.status == 200

    resp_json = await resp.json()
    assert 'token' in resp_json

async def test_fixture_post(test_cli, token):
    # write post
    custom_log('WRITE POST')
    resp = await test_cli.post('/posts/',
        headers = {
            'authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }, json={
            'name': '디미청원을 써주세요',
            'content': '꼭 써주세요 선생님~ ^~^',
            'topic': '테스트',
            # 'image': 'https://www.dimigo.hs.kr/layouts/minimal_dimigo/static/dimigo_logo_white.png'
        })
    assert resp.status == 200
    resp_json = await resp.json()
    post_id = resp_json.get('post_id')
    assert post_id

    # view post
    async def view_post(status=200):
        custom_log('VIEW POST')
        resp = await test_cli.get('/posts/{}'.format(post_id),
            headers = {
                'authorization': 'Bearer {}'.format(token),
                'content-type': 'application/json'
            })
        assert resp.status == status
        if resp.status == 200:
            resp_json = await resp.json()
            print(resp_json)
    
    await view_post()

    # edit post
    # custom_log('EDIT POST')
    # resp = await test_cli.put('/posts/{}'.format(post_id),
    #     headers = {
    #         'authorization': 'Bearer {}'.format(token),
    #         'content-type': 'application/json'
    #     }, json={
    #         'name': '수정해버렸다.'
    #     })
    # assert resp.status == 200

    # view post
    # await view_post()

    # delete post
    # custom_log('DELETE POST')
    # resp = await test_cli.delete('/posts/{}'.format(post_id),
    #     headers = {
    #         'authorization': 'Bearer {}'.format(token),
    #         'content-type': 'application/json'
    #     })
    # assert resp.status == 200

    # view post
    # await view_post(404)
