from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.UserRegisterView, name='register'),
    #path('login/', views.UserLoginView, name='login'),
]