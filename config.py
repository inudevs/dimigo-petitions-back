import os


class Config(object):
    API_VERSION = '0.0.1'
    API_TITLE = '🗳️ Dimigo-Petitions API'
    API_DESCRIPTION = '선배님들의 허락을 받으면, 전통을 바꿀 수 있습니다.'

    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_SECRET_KEY = os.urandom(24)
    MONGO_URI = ''


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 5000
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DB = 'test'
