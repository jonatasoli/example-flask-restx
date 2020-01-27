from flask import Flask
from flask_moment import Moment

moment = Moment()


def init_app(app: Flask):
    moment.init_app(app)
