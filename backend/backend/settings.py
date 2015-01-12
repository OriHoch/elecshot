
import os
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ph-fydzq$bl^$6)t0skl$y#zm+fw-nl*8g^1u$o(#_-ag0_@el'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'corsheaders',
    'backend',
    'candidates'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'backend.urls'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'backend.jwt_payload_handler',
    'JWT_EXPIRATION_DELTA': timedelta(hours=48),
}

DATABASES = {
    'default': {
        'NAME': 'dev.db',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = '/static/'

try:
    from local_settings import *
except ImportError:
    pass
