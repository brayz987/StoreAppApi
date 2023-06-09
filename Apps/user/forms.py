from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ("address",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUserModel
        fields = ("address",)