from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from realbuy_app.models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'username'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'password1'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'password2'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
        
class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'usernameedit'}))
    '''is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'superuseredit'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'staffedit'}))'''
    
    class Meta:
        model = Profile
        fields = ('user', 'email','image','phone','address')
        
        
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'id':'email-register'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'usernameedit'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'superuseredit'}))
    
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')