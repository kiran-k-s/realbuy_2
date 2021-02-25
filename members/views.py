from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm,PasswordChangingForm,LoginForm#EditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.forms.models import model_to_dict

User = get_user_model()


def UserRegisterView(request):
    if request.is_ajax():
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            print(form.errors)
            context = {'form': form }
            data = form.errors.as_json()
            print(data)
            return JsonResponse({
                 'message': 'error','registerform': data
            })
            #return render(request, "realbuy_app/unsuccess.html",context)
    
def UserLoginView(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.is_ajax():
        form = LoginForm(request.POST or None)
        print(request.user.is_authenticated)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                User = get_user_model()
                user_queryset = User.objects.all().filter(email__iexact=username)
                if user_queryset:
                    username = user_queryset[0].username
                    user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                
                return redirect('add1')
            else:
                print("error....")
        else:
            
            print(form.errors)
            # data = model_to_dict(form)
            # print(data)

            # data = model_to_dict(form, fields=[field.name for field in form._meta.fields])
            # print(data)

            #data = form.values()[0]

            data = form.errors.as_json()
            print(data)
            return JsonResponse({
                 'message': 'error','loginform': data
            })
            
    else:    
        return render(request, "members/login.html",context)    

    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
    
    

