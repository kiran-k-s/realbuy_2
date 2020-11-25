from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'usernameedit'}))
    is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'superuseredit'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'staffedit'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser', 'is_staff')
        
        
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'id':'email-register'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'usernameedit'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'superuseredit'}))
    
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')