import pytest
from flask import Flask

import config_testing
from ext.app_factory import create_app
from ext.db import db


@pytest.fixture(scope='session')
def app():
    app_ = create_app(config_testing)
    app_.testing = True
    with app_.test_request_context() as _:
        yield app_


@pytest.fixture
def db_session(app):
    db.create_all()
    yield db.session
    db.drop_all()


@pytest.fixture
def client(app: Flask):
    with app.test_client() as c:
        yield c


@pytest.fixture
def flask_session(client):
    with client.session_transaction() as sess:
        yield sess
