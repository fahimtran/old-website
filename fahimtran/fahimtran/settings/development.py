from .base import *

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
