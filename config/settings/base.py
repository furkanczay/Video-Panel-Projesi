from pathlib import Path
import os
import environ

# DJANGO-ENVIRON OPTION
env = environ.Env()

# BASE_DIR OPTION
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET_KEY OPTION
SECRET_KEY = env('SECRET_KEY')

# ALLOWED HOSTS OPTION
ALLOWED_HOSTS = []

# INSTALLED APPS OPTION
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # APPS
    'apps.core',
    # ADMIN
    'apps.manager',
]

# AUTH USER MODEL OPTION
AUTH_USER_MODEL = 'core.Users'

# AUTHENTICATION BACKENDS OPTION
AUTHENTICATION_BACKENDS = [
    'apps.core.backends.UsersModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# LOGIN/LOGOUT URLS OPTION
LOGIN_REDIRECT_URL = 'homepage'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
PASSWORD_RESET_TIMEOUT = 259200

# MIDDLEWARES OPTION
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT URLCONFIGURATION OPTION
ROOT_URLCONF = 'config.urls'

# TEMPLATES OPTION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

# WSGI OPTION
WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORD VALIDATORS OPTION
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


# LANGUAGES OPTION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# DATE/DATETIME FORMAT OPTION
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i:s'

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',
]
DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%M:%S'
]


# STATIC FILES OPTION
STATIC_URL = 'assets/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'assets/static'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/static_files/')

# MEDIA FILES OPTION
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media/')
MEDIA_URL = '/media/'


# DEFAULT PRIMARY KEY OPTION
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
