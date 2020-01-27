import logging
import traceback

from flask import Flask
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api()


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404


def init_app(app: Flask):
    api.init_app(app, version='1.0', title='Partyou API',
                 description='This a example API change-me description and Title', )
