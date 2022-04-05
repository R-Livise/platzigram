from .default import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']

# manage.py collectstatic
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'