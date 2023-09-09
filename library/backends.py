from django.contrib.auth.backends import ModelBackend
from user.models import MyUser  # Import your custom user model

class MyUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None
