
from django.contrib import admin
from django.urls import path,include
from school_details.views import register_request
from django.conf import settings
from django.conf.urls.static import static
from school_details.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('',include('school_details.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  