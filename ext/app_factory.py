import locale
import logging
import os
from logging import Formatter
from logging.handlers import RotatingFileHandler

from flask import Flask

import config as default_config
from ext import migrate, blueprints_factory, logger_factory
from ext.db import db
from ext.marshmallow import ma
from ext.moment import moment
from ext.redis import redis_store
from ext.restlib import api


def create_app(config=None) -> Flask:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")  # set locale
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    if config is None:
        config = default_config

    app.config.from_object(config)

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    moment.init_app(app)
    redis_store.init_app(app, charset="utf-8", decode_responses=True)

    # Blueprints and API Namespaces
    app = blueprints_factory.register_blueprints(app)
    api.init_app(app)

    loghandler = RotatingFileHandler(os.path.join(app.config.get("BASEDIR"), "logs", "partyou.log"))
    loghandler.setFormatter(Formatter(
        "%(asctime)s %(levelname)s: %(message)s "
        "[in %(pathname)s:%(lineno)d]"
    ))
    

    app.logger.addHandler(loghandler)
    app.logger.setLevel(logging.INFO)

    app = logger_factory.create_logger(app)

    return app
