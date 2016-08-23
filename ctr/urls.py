from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^treinamento/$', views.treinamentos, name="treinamentos"),
    url(r'^efetuar_matricula/(?P<pk_treinamento>\d+)/$', views.efetuar_matricula, name='efetuar_matricula'),
]
