from pathlib import Path
import os
import sys
from celery import Celery



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cmck!^ke6l%7#4qt8%-%&i1k$qcogq8s6l1wd0s2hq0b)so1$1'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'school_details',

]

DATE_INPUT_FORMATS = ['%d-%m-%Y']


CRISPY_TEMPLATE_PACK = 'bootstrap4' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'school2.urls'

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
        },
    },
]

WSGI_APPLICATION = 'school2.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'school_details.CustomUser'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    
]

    

SESSION_EXPIRE_AT_BROWSER_CLOSE = None


AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']


SESSION_COOKIE_AGE = 60 * 60 * 24 * 30


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

STATIC_ROOT=os.path.join(BASE_DIR,'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'post_office.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"
# Email
EMAIL_HOST='localhost'
EMAIL_PORT=587
EMAIL_HOST_USER= 'resilradhakrishnan@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD='nbmczqcjivugbwlr   '
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_SUBJECT_PREFIX = '[Test mail]'


# CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'