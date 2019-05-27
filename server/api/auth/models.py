user_model = {
    'idx': int,
    'name': str,
    'grade': str,
    'klass': str,
    'number': str,
    'serial': str,
    'photo': str,
    'email': str,
    'user_type': str
}

login_model = {
    'token': str,
    'refresh_token': str,
    'user': user_model
}
