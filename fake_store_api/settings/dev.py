from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "Hello_dont_share_this_key_with_anyone_ok"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIR = os.path.join(BASE_DIR, 'static')