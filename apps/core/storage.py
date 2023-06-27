from django_bunny_storage.storage import BunnyStorage
from django.conf import settings


class BunnyCDNStorage(BunnyStorage):
    def url(self, name):
        return f'{settings.MEDIA_URL}{name}'
