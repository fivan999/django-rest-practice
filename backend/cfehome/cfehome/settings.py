import os
import pathlib

import dotenv


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

dotenv.load_dotenv()
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', default='default')

YES_OPTIONS = ('true', 'y', '1', 'yes')

DEBUG = os.getenv('DJANGO_DEBUG', default='True').lower() in YES_OPTIONS

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = os.getenv(
        'DJANGO_ALLOWED_HOSTS', default='127.0.0.1'
    ).split()

INTERNAL_IPS = os.getenv('DJANGO_INTERNAL_IPS', default='127.0.0.1').split()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'algoliasearch_django',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'djoser',
    'products.apps.ProductsConfig',
    'users.apps.UsersConfig',
    'search.apps.SearchConfig',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

ROOT_URLCONF = 'cfehome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'cfehome.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

USER_IS_ACTIVE = (
    os.getenv('USER_IS_ACTIVE', default='true').lower().strip() in YES_OPTIONS
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.'
    'LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

ALGOLIA = {
    'APPLICATION_ID': os.getenv('ALGOLIA_APPLICATION_ID', 'app_id'),
    'API_KEY': os.getenv('ALGOLIA_API_KEY', 'api_key'),
}

CORS_ALLOWED_ORIGINS = []
if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:8111',
        'https://localhost:8111',
    ]
CORS_URLS_REGEX = r"^/api/.*$"

CELERY_TASK_ALWAYS_EAGER = (
    os.getenv('CELERY_TASK_ALWAYS_EAGER', default='true').lower().strip()
    in YES_OPTIONS
)

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', default='localhost')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', default='guest')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', default='password')
CELERY_BROKER_URL = (
    f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:5672//'
)

if os.getenv('USE_SMTP', default='False').lower() in YES_OPTIONS:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_USE_TLS = (
        os.getenv('EMAIL_USE_TLS', default='true').lower() in YES_OPTIONS
    )
    EMAIL_USE_SSL = (
        os.getenv('EMAIL_USER_SSL', default='false').lower() in YES_OPTIONS
    )
    if EMAIL_USE_TLS:
        EMAIL_USE_SSL = False
    if EMAIL_USE_SSL:
        EMAIL_USE_TLS = False
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    SERVER_EMAIL = EMAIL_HOST_USER
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
