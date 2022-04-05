from .default import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ os.environ.get('DJANGO_ALLOWED_HOSTS'),'localhost']

INSTALLED_APPS = INSTALLED_APPS + ['storages']

DEFAULT_FILE_STORAGE = 'platzigram.backend.AzureMediaStorage'
STATICFILES_STORAGE  = 'platzigram.backend.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_STORAGE_KEY = os.environ.get('AZURE_STORAGE_KEY', False)
AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
AZURE_CUSTOM_DOMAIN_URL = os.environ.get('AZURE_CUSTOM_DOMAIN_URL')
AZURE_MEDIA_CONTAINER = os.environ.get('AZURE_MEDIA_CONTAINER', 'media')
AZURE_STATIC_CONTAINER = os.environ.get('AZURE_STATIC_CONTAINER', 'static')

AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.{AZURE_CUSTOM_DOMAIN_URL}'  # Files URL

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'
