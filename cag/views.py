# coding=utf-8

from django.shortcuts import render
from django.views.generic import ListView
from .models import Empresa, Regional, Agencia

class EmpresaList(ListView):

    template_name = 'cag/empresa/empresas.html'
    model = Empresa
    context_object_name = 'empresas'

class RegionalList(ListView):

    template_name = 'cag/regional/regionais.html'
    model = Regional
    context_object_name = 'regionais'

class AgenciaList(ListView):

    template_name = 'cag/agencia/agencias.html'
    model = Agencia
    context_object_name = 'agencias'

empresas = EmpresaList.as_view()
regionais = RegionalList.as_view()
agencias = AgenciaList.as_view()
