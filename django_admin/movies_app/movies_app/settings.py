import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(', ')

AUTH_USER_MODEL = "movies.User"

AUTHENTICATION_BACKENDS = [
    'movies_app.auth.CustomBackend',
]

AUTH_API_LOGIN_URL = "http://auth-service:8010/api/v1/login/"

INTERNAL_IPS = ['127.0.0.1']

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'movies_app.urls'

WSGI_APPLICATION = 'movies_app.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

PAGINATE_BY = os.environ.get('PAGINATE_BY')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

include(
    'components/auth_password_validators.py',
    'components/database.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
)
