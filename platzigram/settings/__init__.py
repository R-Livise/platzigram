import os

if os.environ.get('DJANGO_DEPLOY' )== "prod":
    from .prod import *
else:
    from .dev import *

