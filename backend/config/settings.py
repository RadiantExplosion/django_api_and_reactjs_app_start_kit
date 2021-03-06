import os
from datetime import timedelta
import datetime
import psycopg2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!pp45o$8uagf%rkj79pne099ff=10c-zv-^qndduaua)d@#!wy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
	'www.shiptalent.com',
	'shiptalent.com',
	'staging.shiptalent.com',
	'34.193.87.115',
	'localhost',
	'127.0.0.1',
	'192.168.0.121'
]
# ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
	'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
	'rest_framework_swagger',
    'coreapi'
)

LOCAL_APPS = (
	'authentication',
	'shiptalent_info',
	'talent',
	'talent_position_type',
	'talent_position_sub_type',
    'talent_additional_position_sub_type',
    'talent_picture',
    'talent_resume',
    'talent_video',
	'question',
	'admin_setting',
    'submission',
	'client_casting_request',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shiptalent',
		'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    },
	'OPTIONS': {
        'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static_backend/'
STATIC_ROOT = 'static_backend'

STATICFILES_DIRS = (
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("images", os.path.join(STATIC_ROOT,'images')),
    ("fonts", os.path.join(STATIC_ROOT,'fonts')),
	("rest_framework", os.path.join(STATIC_ROOT,'rest_framework'))
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

AUTH_USER_MODEL = 'authentication.User'
CORS_ORIGIN_ALLOW_ALL = True


# AWS
# If AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are not defined,
# django-s3-upload will attempt to use the EC2 instance profile instead.
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'AKIAJSQZNJJM5VPSXCBQ')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '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')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'talents3')
S3UPLOAD_REGION = os.environ.get('S3UPLOAD_REGION', 'us-east-1')

def create_filename(filename):
    import uuid
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4().hex, ext)
    return os.path.join('custom', filename)


S3UPLOAD_DESTINATIONS = {
    # Allow anybody to upload any MIME type
    'misc': {
        'key': 'uploads/'
    },

    # Allow staff users to upload any MIME type
    'pdfs': {
        'key': 'uploads/pdfs',
        'auth': lambda u: u.is_staff
    },

    # Allow anybody to upload jpeg's and png's. Limit sizes to 5kb - 20mb
    'images': {
        'key': 'uploads/images',
        'auth': lambda u: True,
        'allowed_types': [
            'image/jpeg',
            'image/png'
        ],
        'allowed_extensions': (
            '.jpeg',
            '.jpg',
            '.png',
        ),
        'content_length_range': (5000, 20000000),
    },

    # Allow authenticated users to upload mp4's
    'videos': {
        'key': 'uploads/videos',
        'auth': lambda u: u.is_authenticated,
        'allowed_types': ['video/mp4']
    },

    # Allow anybody to upload any MIME type with a custom name function
    'custom_filename': {
        'key': create_filename
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'request_token': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}