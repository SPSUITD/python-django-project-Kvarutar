
from django import template
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls'))
    #path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
