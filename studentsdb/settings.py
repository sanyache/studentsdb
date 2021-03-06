"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from django.conf import global_settings

#from .env_settings import SECRET_KEY, DEBUG, TEMPLATE_DEBUG, ALLOWED_HOSTS
#from .env_settings import SOCIAL_AUTH_FACEBOOK_SECRET, SOCIAL_AUTH_FACEBOOK_KEY
#from .env_settings import DATABASES, STATIC_URL, MEDIA_URL, MEDIA_ROOT
#from .env_settings import ADMIN_EMAIL, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL
#from .env_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS
#from .env_settings import PORTAL_URL

# in dev envrironment we may not have STATIC_ROOT defined
try:
    from .env_settings import STATIC_ROOT
except ImportError:
    pass


import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-1h6=v&gy+kpl_-)-dmwyvy4cg-1mly^l345n%%*x41=t$+2k%'
LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'
#LOGIN_REDIRECT_URL = 'students/base.html'

LOGGING = {

    'version' : 1,
    'disable_existing_loggers' : True,
    'formatters' : {
        'verbose' : {
            'format' : '%(levelname)s %(asctime)s %(module)s: %(message)s '
        },
        'simple' : {
            'format' : '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'students.views.contact_admin': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '-1h6=v&gy+kpl_-)-dmwyvy4cg-1mly^l345n%%*x41=t$+2k%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PORTAL_URL='http://localhost:8000'
ADMIN_EMAIL = 'tsabiy_viktor@ukr.net'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'sanyache75@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'registration',
    'social_django',
    'social.apps.django_app.default',
    'students',
    'studentsdb',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'studentsdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[ os.path.join(BASE_DIR,  'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		        'social_django.context_processors.backends',
		        'social_django.context_processors.login_redirect',
                'studentsdb.context_processors.students_proc',
		        'students.context_processors.groups_processor',
		        'students.context_processors.lang_processor'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '1383994755018466'
SOCIAL_AUTH_FACEBOOK_SECRET = '1cb77142c268fe54ce89fcc4ec9462d2'
CRISPY_TEMPLATE_PACK='bootstrap3'
WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'..','media')
from db import DATABASES


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
from django.conf import global_settings

REGISTRATION_OPEN = True