from .base import *

# DEBUG MODE OPTION
DEBUG = False

# ROOT URLCONFIGURATION OPTION
ROOT_URLCONF = 'config.urls'

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
    # THIRD-PARTY
    'crispy_forms',
    'crispy_tailwind',
    'django_bunny_storage',
]
