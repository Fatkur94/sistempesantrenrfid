from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils.translation import gettext as _


class UserStaffForm(UserCreationForm):
    error_messages= {
            'duplicate_username': 'maaf username ini sudah terdaftar',
            "password_mismatch": _("Passwords anda tidak cocok.")
    }
    email = forms.EmailField()
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Konfirmasi Password')
    def clean_username(self):
        username = self.cleaned_data["username"]
       
        try:
            User._default_manager.get(username=username)
            #if the user exists, then let's raise an error message

            raise forms.ValidationError( 
              self.error_messages['duplicate_username'],  #user my customized error message
              code='duplicate_username',   #set the error message key
                )
        except User.DoesNotExist:
            return username # great, this user does not exist so we can continue the registration process

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Name Belakang',
        }

class UserSuperUserForm(UserCreationForm):
    email = forms.EmailField()
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Konfirmasi Password')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Name Belakang',
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Name Belakang',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': 'Photo Profile',
        }