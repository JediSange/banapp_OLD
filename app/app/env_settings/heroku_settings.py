import os

ALLOWED_HOSTS = ['0.0.0.0']
API_BASE = os.environ['API_BASE']
API_KEY = os.environ['API_KEY']
API_STATIC_URL = os.environ['API_STATIC_URL']
DEBUG = os.environ['DEBUG']
MONGO_URL = os.environ['MONGOLAB_URI']
SECRET_KEY = os.environ['SECRET_KEY']
TEMPLATE_DEBUG = os.environ['TEMPLATE_DEBUG']
