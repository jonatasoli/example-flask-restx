import os
from datetime import timedelta
from decouple import config


BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEFAULT_TIMEZONE = 'America/Sao_Paulo'

SERVER_NAME = config('SERVER_NAME')


REDIS_HOST = config('REDIS_HOST')
REDIS_PASSWORD = config('REDIS_PASSWORD')
REDIS_URL = "redis://:{}@{}:6379/0".format(REDIS_PASSWORD, REDIS_HOST)

# SLACK BOT ###########################################
SLACK_BOT_TOKEN = config('SLACK_BOT_TOKEN')
SLACK_SEND_MESSAGES = config('SLACK_SEND_MESSAGES', cast=bool)

#########################################################################

# CELERY ###########################################
CELERY_BROKER_URL="redis://{}@{}:6379/0".format(REDIS_PASSWORD, REDIS_HOST)
CELERY_RESULT_BACKEND="redis://{}@{}:6379/0".format(REDIS_PASSWORD, REDIS_HOST)
CELERYD_TASK_SOFT_TIME_LIMIT = config('CELERYD')

# EMAIL_QUEUE = True
PREFERRED_URL_SCHEME = config('URL_SCHEME')

SECRET_KEY = 'TESTING_KEY'
CONFIRMATION_KEY = 'TESTING_CONFIRMATION_KEY'

SESSION_TYPE = "sqlalchemy"
SESSION_USE_SIGNER = config('SESSION_USE_SIGNER', cast=bool)
SESSION_KEY_PREFIX = config('SESSION_KEY_PREFIX')
PERMANENT_SESSION_LIFETIME = timedelta(days=3)

SQLALCHEMY_INCLUDE_SCHEMAS      = config('SQLALCHEMY_INCLUDE_SCHEMAS', cast=bool)
SQLALCHEMY_DATABASE_URI         = 'sqlite:///:memory:'
SQLALCHEMY_MIGRATE_REPO         = os.path.join(BASEDIR, "migrations")
SQLALCHEMY_TRACK_MODIFICATIONS  = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)

UPLOAD_FOLDER = os.path.join(BASEDIR, "uploads")
DOWNLOAD_FOLDER = os.path.join(BASEDIR, "downloads")
ALLOWED_EXTENSIONS = frozenset(["txt", "pdf", "png", "jpg", "jpeg", "gif"])
MAX_CONTENT_LENGTH = 16 * 1440 * 1440
UPLOAD_SIZES = {
    "small": 800,
    "thumb": 480,
    "icon": 320
}

