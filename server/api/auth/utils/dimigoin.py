import json
import requests_async as requests

async def dimigo_auth(id, password):
    res = await requests.post('https://dev-api.dimigo.in/auth', json={
        'id': id,
        'password': password
    })
    if res.status_code != 200:
        return False
    return json.loads(res.text)['token']

async def dimigo_profile(dimigoin_token):
    headers = {
        'content-type': 'application/json',
        'authorization': 'Bearer {}'.format(dimigoin_token)
    }
    res = await requests.get('https://dev-api.dimigo.in/user/jwt', headers=headers)
    if res.status_code != 200:
        return False
    return json.loads(res.text)
