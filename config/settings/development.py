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
