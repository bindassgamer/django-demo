from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from database.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username',
                  'email','password1',
                  'password2'] 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email']
   
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']