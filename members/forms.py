from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from realbuy_app.models import Profile
from django.contrib.auth import authenticate, get_user_model

User = get_user_model() 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'username'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'password1'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'password2'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #       user = user_qs.first()
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                User = get_user_model()
                user_queryset = User.objects.all().filter(email__iexact=username)
                if user_queryset:
                    username = user_queryset[0].username
                    user = authenticate(username=username, password=password)
                    if not user:
                        raise forms.ValidationError("This user doesn't exist")
                else:
                    raise forms.ValidationError("This user doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            
        return super(LoginForm, self).clean(*args, **kwargs)

        
        
'''class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email-register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'usernameedit'}))
    is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'superuseredit'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'id':'staffedit'}))
    
    class Meta:
        model = Profile
        fields = ('user', 'email','image','phone','address') '''
        
        
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'id':'email-register'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'usernameedit'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'superuseredit'}))
    
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')