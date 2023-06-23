from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import Users


class UsersModelBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except Users.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
