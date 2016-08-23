from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^empresa/$', views.empresas, name="empresas"),
    url(r'^regional/$', views.regionais, name="regionais"),
    url(r'^agencia/$', views.agencias, name="agencias"),
]
