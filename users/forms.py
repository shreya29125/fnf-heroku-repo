from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegisterForm(UserCreationForm):
	
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].help_text = 'Use ".", "_" and all alphabets and numbers'

            

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'is_artist', 'first_name', 'last_name']