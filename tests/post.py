import asyncio
import os.path
import json
import sys
import requests_async as requests

async def get_token():
    with open(os.path.join(sys.path[0], 'secret.json')) as secret_file:
        user = json.load(secret_file)
        res = await requests.post('http://localhost:5000/auth/login', json={
            'id': user['id'],
            'password': user['password']
        })
        return json.loads(res.text)['token']

async def test():
    token = await get_token()
    print('[*] token:', token)

    print('\n== Write post ==')    
    res = await requests.post('http://localhost:5000/post/', 
        headers = {
            'authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }, json={
            'name': '연애하게 해주세요',
            'content': '어차피 대부분은 못 할 거예요 ^~^',
            # 'image': 'https://www.dimigo.hs.kr/layouts/minimal_dimigo/static/dimigo_logo_white.png'
        })
    post_id = json.loads(res.text)['post_id']
    print('[*] post_id:', post_id)

    async def view():
        print('\n== View post ==')    
        res = await requests.get('http://localhost:5000/post/{}'.format(post_id),
            headers = {
                'authorization': 'Bearer {}'.format(token),
                'content-type': 'application/json'
            })
        print(res.text)
    
    await view()

    print('\n== Edit post ==')    
    res = await requests.put('http://localhost:5000/post/{}'.format(post_id),
        headers = {
            'authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }, json={
            'name': '연애하지 마세요'
        })
    print(res.status_code)    

    await view()

    print('\n== Delete post ==')
    res = await requests.delete('http://localhost:5000/post/{}'.format(post_id),
        headers = {
            'authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        })
    print(res.status_code)

if __name__ == '__main__':
    asyncio.run(test())
