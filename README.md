# Dimigo-Petitions
Python의 비동기 웹 프레임워크인 Sanic을 사용

## Login with Dimigo ID
디미고 계정으로 로그인
- 공개 디미고인 API를 이용해서 인증

### request
```json
{
    "id": "test",
    "password": "test"
}
```

- `id`: 사용자 아이디
- `password`: 사용자 비밀번호

### response
```json
{
    "token": "(JWT 토큰)",
    "refresh_token": "-",
    "user": {
        "idx": 0,
        "name": "test",
        "grade": "1",
        "klass": "5",
        "number": "20",
        "serial": "1520",
        "photo": null,
        "email": "test@civar.dev",
        "user_type": "S"
    }
}
```

- `token`: JWT 토큰
- `refresh_token`
- `user`
  - `idx`: 디미고인 계정에서의 idx(무시)
  - `name`: 학생 이름
  - `grade`: 학생 학년
  - `klass`: 학생 반
  - `number`: 학생 번호
  - `serial`: 학번
  - `photo`: 학생 사진
  - `email`: 학생 이메일
  - `user_type`: 회원 종류(학생은 `S`)
