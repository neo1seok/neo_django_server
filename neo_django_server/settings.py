"""
Django settings for neo_django_server project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import logging
import os
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(2yt5c#(a2ip8x38u#6lbncvvd1%kq^9cxd3ln&kqy^m&kum)l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'oauth2_provider',#python oauth2 설치 , admin 화면에  acces token 내용 추가 , migrate 를 해줘야 됨
    'password',
    'access',
    'comm',
    'main',
    'health',
    'webtoon',
    'private_link',
    'jcsg',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'neo_django_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'comm','templates') ],
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
REST_FRAMEWORK_ = {
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

WSGI_APPLICATION = 'neo_django_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'neo_django_server',  # DB명
         'USER': 'neo1seok',  # 데이터베이스 계정
         'PASSWORD': 'tofhdna1pi',  # 계정 비밀번호
        'HOST': 'localhost',  # 데이테베이스 주소(IP)
        #'HOST': '192.168.219.17',  # 데이테베이스 주소(IP)
         'PORT': '3306',  # 데이터베이스 포트(보통은 330
         # 'OPTIONS': {
         #     'read_default_file': 'my.cnf',
         # },
     },
    # 'default_': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/


TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#STATIC_URL = '/static/'
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
STATICFILES_DIRS = [
    BASE_DIR + "/static",
]
print("BASE_DIR",BASE_DIR)
print("STATICFILES_DIRS",STATICFILES_DIRS)

LOGIN_URL = '/access/login/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = '/'
LOG_FILE = os.path.join(BASE_DIR,"logs" ,'server.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file','console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file','console'],
            'propagate': False,
            'level': 'INFO',
        },
        'jcsg.views': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
        },

    }
}
