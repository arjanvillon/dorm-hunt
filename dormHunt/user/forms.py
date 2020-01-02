from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User, UserProfile
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta():
        model = User
        fields = ('user_type', 'username', 'email', 'password1', 'password2')

class UserAuthenticationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'validate':''}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'validate':''}))

    class Meta():
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login details supplied!")

class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta():
        model = UserProfile
        fields = ('first_name', 'last_name', 'number', 'birthday', 'emergency_name', 'emergency_phone', 'picture')
