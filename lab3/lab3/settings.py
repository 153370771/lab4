import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import os.path 
import sae.const
from os import environ
debug = not environ.get("APP_NAME", "") 
if debug:
    MYSQL_DB = 'BookDB'    
    MYSQL_USER = 'root' 
    MYSQL_PASS = '123456' 
    MYSQL_HOST_M = '127.0.0.1' 
    MYSQL_HOST_S = '127.0.0.1' 
    MYSQL_PORT = '3306' 
else: 
    import sae.const 
    MYSQL_DB = sae.const.MYSQL_DB 
    MYSQL_USER = sae.const.MYSQL_USER 
    MYSQL_PASS = sae.const.MYSQL_PASS 
    MYSQL_HOST_M = sae.const.MYSQL_HOST 
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
    MYSQL_PORT = sae.const.MYSQL_PORT
"""
Django settings for lab3 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=$@qdlp=$bt)v_^*xghv!$thbsfl85!)f9-2*k90&$m_iz5zt@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lab3.urls'

WSGI_APPLICATION = 'lab3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':MYSQL_DB,
        'USER':MYSQL_USER,
        'PASSWORD':MYSQL_PASS,
        'HOST':MYSQL_HOST_M,
        'PORT':MYSQL_PORT,
    }
}
STATIC_PATH = os.path.join(os.path.dirname(__file__), '../media').replace('\\','/')
TEMPLATE_DIRS = (
    './blog/',
    os.path.join(BASE_DIR, '../templates').replace('\\', '/'),
    BASE_DIR + '/templates/',
    )
STATICFILES_DIRS = (
    './blog/',os.path.join(BASE_DIR,'../images').replace('\\','/'),
    BASE_DIR + '/images/', 
    
)


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH=False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
