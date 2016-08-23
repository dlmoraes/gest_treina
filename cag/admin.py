# coding=utf-8

from django.contrib import admin
from cag.models import Empresa, Regional, Agencia

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'dt_criado', 'dt_modificado']
    list_filter = ['nome', 'sigla']
    list_display_links = ['sigla']

@admin.register(Regional)
class RegionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'dt_criado', 'dt_modificado']
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'regional', 'empresa', 'dt_criado']
    list_filter = ['regional', 'empresa']
    prepopulated_fields = {'slug' : ('nome',)}
    search_fields = ['nome']
