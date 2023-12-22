"""
Django settings for django_words project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import pyaml
import platform
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&ho^g(zjf*cqet*n2ek*a49c%mu$a!w$z)bgiu+s4qzth7=!oi'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-&ho^g(zjf*cqet*n2ek*a49c%mu$a!w$z)bgiu+s4qzth7=!oi')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if platform.system().lower() == 'linux':
    DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mdeditor',
    'ebbinghaus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'my_middleware.cors_middleware.CorsMiddleware',
]

ROOT_URLCONF = 'django_words.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'django_words.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
}
if platform.system().lower() == 'linux':
    with open(f'{BASE_DIR}/config/database.yaml', 'r', encoding='utf-8') as f:
        database = pyaml.yaml.safe_load(f)
        if database:
            DATABASES['default'] = database

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 关闭时区

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/word_static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'word_static')
STATICFILES_DIRS = ['word_static']

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/word_media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MDeditor
X_FRAME_OPTIONS = 'SAMEORIGIN'

# 日志配置
LOG_DIR = os.path.join(BASE_DIR, 'log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'ebbinghaus': {
            'level': 'INFO',  # 设置日志级别
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'ebbinghaus.log'),
            'maxBytes': 1024 * 1024 * 5,  # 设置日志文件大小上限
            'backupCount': 5,  # 设置备份日志文件的数量
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',  # 设置日志级别
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 1024 * 1024 * 5,  # 设置日志文件大小上限
            'backupCount': 5,  # 设置备份日志文件的数量
            'formatter': 'standard',
            'encoding': 'utf-8',
        }
    },
    'loggers': {
        '': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'ebbinghaus': {
            'handlers': ['ebbinghaus'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
}

