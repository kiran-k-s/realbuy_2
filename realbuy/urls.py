
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('realbuy_app.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    
    #url(r'^select2/', include('select2.urls')),
    
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
