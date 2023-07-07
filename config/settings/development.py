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