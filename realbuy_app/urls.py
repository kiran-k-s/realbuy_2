from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('home', views.index, name='home'),
    path('recent', views.RecentView, name='recent'),
    path('detail/<int:pk>', views.DetailView, name='detail')
    path('add1/', views.AddView1, name='add1'),
    path('add2/', views.AddView2, name='add2'),
    
    url(r'^api/contacts/$', views.contacts_list),
    url(r'^api/contacts/(?P<pk>[0-9]+)$', views.contacts_detail)
]
