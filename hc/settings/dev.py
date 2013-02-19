"""Settings for Development Server"""
from hc.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/hc'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hc',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# WSGI_APPLICATION = 'hc.wsgi.dev.application'
