"""
Setup CELERY
Celery Configuration Options
"""
from utils.configs_loader import load_configs
from datetime import timedelta
from celery.schedules import crontab

configs = load_configs()

CELERY_TIMEZONE = 'Asia/Bangkok'
CELERY_CREATE_MISSING_QUEUES = True


DEFAULT_REDIS_CELERY = {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0,
    'PASSWORD': None,
}
REDIS_CELERY = getattr(configs, 'REDIS_CELERY', DEFAULT_REDIS_CELERY)

if REDIS_CELERY.get('PASSWORD', None):
    BROKER_URL = 'redis://:{}@{}:{}/{}'.format(REDIS_CELERY.get('PASSWORD', None), REDIS_CELERY['HOST'], REDIS_CELERY.get('PORT', 6379), REDIS_CELERY.get('DB', 0))
else:
    BROKER_URL = 'redis://{}:{}/{}'.format(REDIS_CELERY['HOST'], REDIS_CELERY.get('PORT', 6379), REDIS_CELERY.get('DB', 0))

CELERY_RESULT_BACKEND = BROKER_URL  # result from tasks
CELERY_TASK_RESULT_EXPIRES = timedelta(hours=12)
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Bangkok'
CELERY_CREATE_MISSING_QUEUES = True

CELERY_ROUTES = {

}

CELERY_ANNOTATIONS = {

}

CELERYBEAT_SCHEDULE = {

}

BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': getattr(configs, 'CELERY_VISIBILITY_TIMEOUT', 3600),
}
CELERY_ALWAYS_EAGER = getattr(configs, 'CELERY_ALWAYS_EAGER', False)  # Set True For Internal Test Celery

# other celery / redis settings below this line