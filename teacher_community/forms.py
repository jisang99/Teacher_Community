from django.contrib.auth.forms import UserCreationForm
from .models import Teacher

class SignupForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username', 'password1', 'password2', 'license')
