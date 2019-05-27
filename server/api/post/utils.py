from datetime import datetime

def timestamp():
    return int(datetime.now().timestamp())

def hide_id(id):
    return id[0] + len(id) * '*'
