import sys

from proj.settings.default import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tbd(pv7679n_w-t++*s_*oon&#v0ubhkxhzvlq51ko2+=dt*z#'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoserviceskeleton',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
    },
}

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.sqlite3',
            'NAME':     'test_database.sqlite',
        },
    }