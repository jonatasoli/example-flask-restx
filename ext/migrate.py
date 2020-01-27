from flask import Flask
from flask_migrate import Migrate

migrate = Migrate()


def init_app(app: Flask, db):
    migrate.init_app(app, db)
