from copy import name

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.static import serve as serve_static
from django.conf.urls.static import static
from core import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^controle_agencia/', include('cag.urls', namespace='cag')),
    url(r'^controle_atendente/', include('cat.urls', namespace='cat')),
    url(r'^controle_treinamento/', include('ctr.urls', namespace='ctr')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )