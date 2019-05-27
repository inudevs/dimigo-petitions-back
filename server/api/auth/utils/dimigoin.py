import json
import requests_async as requests

async def dimigo_auth(_id, _password):
    res = await requests.post('https://dev-api.dimigo.in/auth', json={
        'id': _id,
        'password': _password
    })
    if res.status_code != 200:
        return False
    return json.loads(res.text)['token']

async def dimigo_profile(_token):
    headers = {
        'content-type': 'application/json',
        'authorization': 'Bearer {}'.format(_token)
    }
    res = await requests.get('https://dev-api.dimigo.in/user/jwt', headers=headers)
    if res.status_code != 200:
        return False
    return json.loads(res.text)
