"""
Django settings for herokuTest project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
import cloudinary
# import cloudinary.uploader
# import cloudinary.api
import cloudinary_storage

# LOGGING = {
# 'version': 1,
# 'disable_existing_loggers': False,
# 'formatters': {
#     'verbose': {
#         'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
#                    'pathname=%(pathname)s lineno=%(lineno)s '
#                    'funcname=%(funcName)s %(message)s'),
#         'datefmt': '%Y-%m-%d %H:%M:%S'
#     },
#     'simple': {
#         'format': '%(levelname)s %(message)s'
#     }
# },
# 'handlers': {
#     'null': {
#         'level': 'DEBUG',
#         'class': 'logging.NullHandler',
#     },
#     'console': {
#         'level': 'INFO',
#         'class': 'logging.StreamHandler',
#         'formatter': 'verbose'
#     }
# },
# 'loggers': {
#     'django': {
#         'handlers': ['console'],
#         'level': 'DEBUG',
#         'propagate': True,
#     },
#     'django.request': {
#         'handlers': ['console'],
#         'level': 'DEBUG',
#         'propagate': False,
#     },
# }}


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# WHITENOISE_AUTOREFRESH = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*@8omwg16h%ht*mmad^c4*0h5(v8lba1ruoyxjwy46-_vdz1nv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'newapp',
    'cloudinary',
    'cloudinary_storage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'herokuTest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'herokuTest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['shathrawan.com', 'http://www.shathrawan.com', 'www.shathrawan.com', 'https://www.shathrawan.com', 'shathrwan.herokuapp.com', 'https://shathrwan.herokuapp.com',  'https://desolate-stream-43784.herokuapp.com/', 'desolate-stream-43784.herokuapp.com', '127.0.0.1', 'http://127.0.0.1/']
# ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'photos')
MEDIA_URL = '//photos/'

# Activate Django-Heroku.
# django_heroku.settings(locals())

# django_heroku.settings(config=locals(), staticfiles=False,logging=False)
# cloudinary.config(
#   cloud_name = "hgfcbzcmp",
#   api_key = "482516611123756",
#   api_secret = "ULa6vI61Q8UYE8PQ1OWYorT_Ozc"
# )

cloudinary.config(
  cloud_name = "hcvmhvlwk",
  api_key = "813159883675153",
  api_secret = "ND4WL_pjstEtz5AF-jhPW_l0u4w",
  secure = True
)

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'hgfcbzcmp',
#     'API_KEY': '482516611123756',
#     'API_SECRET': 'ULa6vI61Q8UYE8PQ1OWYorT_Ozc',
# }

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'