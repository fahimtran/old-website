from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'fahimtran.com',
    'www.fahimtran.com',
    'pure-faculty-274606.uc.r.appspot.com',
    '127.0.0.1',
    'localhost',
]

# SECURITY: To secure payloads and user information
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
