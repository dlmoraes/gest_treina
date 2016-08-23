# coding=utf-8

from django.contrib import admin
from .models import Cargo, Pessoa, Atendente

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'dt_criado', 'dt_modificado']
    list_filter = ['nome']
    search_fields = ['nome']

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'dta_nascimento', 'doc_cpf', 'doc_rg']
    search_fields = ['nome', 'doc_cpf', 'doc_rg']

@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):

    list_display = ['matricula', 'pessoa', 'dta_entrevista', 'dta_contratacao', 'cargo', 'situacao', 'agencia']
    list_filter = ['cargo', 'situacao']
    search_fields = ['matricula', 'pessoa', 'agencia']
