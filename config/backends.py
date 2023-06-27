from django.contrib.auth.backends import ModelBackend
from apps.core.models import Users


class PasswordlessAuthBackend(ModelBackend):
    def authenticate(self, email=None):
        try:
            return Users.objects.get(email=email)
        except Users.DoesNotExist:
            return None
