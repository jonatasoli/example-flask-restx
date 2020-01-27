from flask import Flask
from flask_redis import FlaskRedis

redis_store = FlaskRedis()


def init_app(app: Flask):
    redis_store.init_app(app)
