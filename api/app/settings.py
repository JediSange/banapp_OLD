# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Local settings
try:
    from local_settings import *
except Exception as e:
    ALLOWED_HOSTS = ['0.0.0.0']
    API_BASE = os.environ['DEBUG']
    API_KEY = os.environ['DEBUG']
    API_STATIC_URL = os.environ['DEBUG']
    DEBUG = os.environ['DEBUG']
    MONGO_URL = os.environ['MONGOLAB_URI']
    SECRET_KEY = os.environ['SECRET_KEY']
    TEMPLATE_DEBUG = os.environ['DEBUG']

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

# Database
import mongoengine
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

SESSION_ENGINE = 'mongoengine.django.sessions'

if 'MONGO_URL' in locals():
    mongoengine.connect('banapp', host=MONGO_URL)
else:
    mongoengine.connect('banapp')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)

# Templates
TEMPLATE_DIRS = (
  os.path.join(BASE_DIR, 'templates'),
)
