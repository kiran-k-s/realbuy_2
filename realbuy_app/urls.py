from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('home', views.index, name='home'),
    path('recent', views.RecentView, name='recent'),
    path('detail/<int:pk>', views.DetailView, name='detail')
    path('add1', views.AddView1, name='add1'),
    path('add2', views.AddView2, name='add2'),
    path('contactus', views.ContactUs, name='contactus')
    path('category_recent/<str:cats>/', views.CategoryViewRecent, name='category_recent'),
    path('category_filter/<str:cats>/', views.CategoryViewFilter, name='category_filter'),
    path('update1/<int:pk>', views.UpdateView1, name='update1')
    path('update2/<int:pk>', views.UpdateView2, name='update2')
    path('delete/<int:pk>', views.DeleteView, name='delete')
    
    
    url(r'^api/contacts/$', views.contacts_list),
    url(r'^api/contacts/(?P<pk>[0-9]+)$', views.contacts_detail)
]
