from django.contrib.auth.backends import ModelBackend
from apps.core.models import Users


class PasswordlessAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, **kwargs):
        try:
            return Users.objects.get(email=email)
        except Users.DoesNotExist:
            return None
