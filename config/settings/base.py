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

# CRISPY FORMS OPTION
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

# AUTH USER MODEL OPTION
AUTH_USER_MODEL = 'core.Users'

# AUTHENTICATION BACKENDS OPTION
AUTHENTICATION_BACKENDS = [
    'config.backends.PasswordlessAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# LOGIN/LOGOUT URLS OPTION
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'login'
PASSWORD_RESET_TIMEOUT = 259200
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

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

# BUNNY CDN STORAGE OPTION

DEFAULT_FILE_STORAGE = 'apps.core.storage.BunnyCDNStorage'
MEDIA_URL = env('MEDIA_URL')
BUNNY_USERNAME = env('BUNNY_USERNAME')
BUNNY_PASSWORD = env('BUNNY_PASSWORD')
BUNNY_REGION = env('BUNNY_REGION')

# LANGUAGES OPTION
LANGUAGE_CODE = 'tr-TR'

TIME_ZONE = 'Europe/Istanbul'

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
# MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media/')
# MEDIA_URL = '/media/'


# SMTP EMAIL OPTION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# WEBHOOK OPTION
WEBHOOK_URL = env('WEBHOOK_URL')

# DEFAULT PRIMARY KEY OPTION
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
