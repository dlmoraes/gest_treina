# coding=utf-8
from datetime import date
from django.db import models
from django.urls import reverse_lazy

from core.models import ControleTemporal
from core.lists import SITUACAO_CHOICES

class Prazo(ControleTemporal):

    nome = models.CharField(max_length=15, unique=True)
    qtd_dia = models.IntegerField('Quantidade de dias')
    dia_util = models.BooleanField(verbose_name='Dia útil', default=False, help_text='Contabilizar apenas os dias úteis')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Treinamento(ControleTemporal):

    TIPO_TREINAMENTO = (
        ('inicial', 'Inicial'),
        ('rotina', 'Rotina'),
    )

    titulo = models.CharField('Título', max_length=50)
    slug = models.SlugField('Atalho', max_length=50)
    descricao = models.TextField('Descrição', null=True, blank=True)
    tipo = models.CharField(max_length=25, choices=TIPO_TREINAMENTO)
    prazo = models.ForeignKey(Prazo)
    status = models.CharField(max_length=2, choices=SITUACAO_CHOICES, default='AT')


    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return '{} [{}]'.format(self.titulo, self.titulo)

    def get_matricular_no_treinamento(self):
        return reverse_lazy('ctr:efetuar_matricula', kwargs=dict(pk_treinamento=self.id))

class MatriculaManager(models.Manager):

    def matricular(self, matricula_key, treinamento, pessoa):
        matricula = Matricula.objects.create(matricula_key=matricula_key, treinamento=treinamento, pessoa=pessoa)
        return matricula

class Matricula(ControleTemporal):

    matricula_key = models.CharField('Chave da matricula', max_length=40, db_index=True)
    treinamento = models.ForeignKey(Treinamento, related_name='treinamentos')
    pessoa = models.ForeignKey('cat.Pessoa', related_name='pessoas')

    objects = MatriculaManager()

    class Meta:
        ordering = ['treinamento', 'pessoa']
        unique_together = (('matricula_key', 'treinamento', 'pessoa'),)

