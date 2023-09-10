from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email',)