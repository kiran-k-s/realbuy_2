from . import views
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView, name='edit_profile'),
    path('password/', views.PasswordsChangeView, name='password_change'),
    path('login_page/', views.UserLoginView, name='login_page'),
]