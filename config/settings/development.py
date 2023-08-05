from .base import *

# DEBUG MODE OPTION
DEBUG = True

# DATABASES OPTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ROOT URLCONFIGURATION OPTION
ROOT_URLCONF = 'config.dev_urls'

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
    'apps.modules.useful_links',
    # ADMIN
    'apps.manager',
    # THIRD-PARTY
    'crispy_forms',
    'crispy_tailwind',
    'django_bunny_storage',
    'ckeditor',
]
