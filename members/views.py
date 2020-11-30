from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditForm, PasswordChangingForm,LoginForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login_page')
    
def UserLoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('add1')
        else:
            print("error....")
            
    return render(request, "members/login_page.html",context)

    
class UserEditView(generic.UpdateView):
    form_class = EditForm
    template_name = 'members/edit_profile.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
def Profile(request):
    return render(request, 'profile.html',{})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
    
    

