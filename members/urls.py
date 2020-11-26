from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.UserRegisterView, name='register'),
    path('edit_profile/', views.UserEditView, name='edit_profile'),
    path('profile/', views.Profile, name='profile'),
    path('password/', views.PasswordsChangeView, name='password_change'),
    
    #path('login/', views.UserLoginView, name='login'),
]