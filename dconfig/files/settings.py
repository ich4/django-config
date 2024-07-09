from .common_settings import *  # pylint: disable=W0401 NOSONAR


INSTALLED_APPS += []

CSRF_TRUSTED_ORIGINS = getattr(configs, 'CSRF_TRUSTED_ORIGINS', [])
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


try:
    from configs import *  # pylint: disable=W0401 NOSONAR
except ImportError:
    pass
