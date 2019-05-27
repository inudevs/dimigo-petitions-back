import asyncio
import os.path
import json
import sys
import requests_async as requests

async def test():
    with open(os.path.join(sys.path[0], 'secret.json')) as secret_file:
        user = json.load(secret_file)
    res = await requests.post('http://localhost:5000/auth/login', json={
        'id': user['id'],
        'password': user['password']
    })
    print(res.text)

if __name__ == '__main__':
    asyncio.run(test())
