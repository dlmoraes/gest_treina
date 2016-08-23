# coding=utf-8

from django.contrib import admin
from .models import Prazo, Treinamento, Matricula

@admin.register(Prazo)
class PrazoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'qtd_dia', 'dia_util', 'dt_criado', 'dt_modificado']
    list_filter = ['dia_util']
    search_fields = ['nome']

class MatriculaInline(admin.StackedInline):
    model = Matricula
    fields = ['pessoa']
    extra = 2

@admin.register(Treinamento)
class TreinamentoAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    prepopulated_fields = {"slug": ('titulo',)}
    list_display = ['titulo', 'tipo', 'prazo', 'descricao']
    search_fields = ['titulo']
    list_filter = ['tipo', 'prazo']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):

    list_display = ['matricula_key', 'treinamento', 'pessoa']
