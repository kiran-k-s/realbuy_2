from . import views
from django.urls import path
from .views import RecentView, DetailedView, FeaturedView, UpdateView1, UpdateView2, DeletePropertyView

urlpatterns = [
    path('', views.Home, name='home'),
    path('category_home1/<str:cats>/', views.CategoryViewHome1, name='category_home1'),
    path('category_home2/', views.CategoryViewHome2, name='category_home2'),
    path('category_filter2/', views.CategoryViewFilter2, name='category_filter2'),
    path('category_filter1/<str:cats>/', views.CategoryViewFilter1, name='category_filter1'),
    path('about_us/', views.AboutUs, name='about_us'),
    path('recent/', RecentView.as_view(), name='recent'),
    path('category_recent/<str:cats>/', views.CategoryViewRecent, name='category_recent'),
    path('featured/',views.FeaturedView, name='featured'),
    path('detail/<int:pk>', DetailedView.as_view(), name='detail'),
    path('add1/', views.AddView1, name='add1'),
    path('add2/', views.AddView2, name='add2'),
    path('contactus/',views.ContactUs, name='contactus'),
    path('update1/<int:pk>', UpdateView1.as_view(), name='update1'),
    path('update2/<int:pk>', UpdateView2.as_view(), name='update2'),
    path('delete/<int:pk>', DeletePropertyView.as_view(), name='delete'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('profile', views.Profile, name='profile'),
    
]
