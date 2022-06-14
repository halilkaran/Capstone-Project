from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

THIRD_PARTY_APPS = [
    "debug_toolbar",
]

INSTALLED_APPS += THIRD_PARTY_APPS


THIRD_PARTY_MIDDLEWARE = [
    # for debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
