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

User = get_user_model()


def UserRegisterView(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login_page')
    else:
        print(form.errors)
        context = {'form': form }
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, "realbuy_app/unsuccess.html",context)
    
# def UserLoginView(request):
#     form = LoginForm()
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         form = LoginForm(request.POST or None)
#         print(request.user.is_authenticated)
#         if form.is_valid():
#             print(form.cleaned_data)
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is None:
#                 User = get_user_model()
#                 user_queryset = User.objects.all().filter(email__iexact=username)
#                 if user_queryset:
#                     username = user_queryset[0].username
#                     user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
                
#                 return redirect('add1')
#             else:
#                 print("error....")
#         else:
#             print(form.errors)
#             context = {'loginform': form }
#             return render(request, "realbuy_app/unsuccess.html",context)
            
#     else:    
#         return render(request, "members/login.html",context)    



def UserLoginView(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
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
            # for field in form:
            #     for problem in field.errors():
            #         messages.error(request, problem)

            # for problem in form.non_field_errors():
            #     messages.error(request, problem)

            
            #messages.error(request, form)
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            url = "{0}/{1}".format(request.META.get('HTTP_REFERER', '/'), {'form':form})

            return HttpResponseRedirect(url)
            
    else:    
        return render(request, "members/login.html",context) 
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
    
    

