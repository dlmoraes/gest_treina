# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.db import models
from core.lists import SITUACAO_CHOICES
from core.models import ControleTemporal

class Empresa(ControleTemporal):
    nome = models.CharField(max_length=100)
    sigla = models.SlugField(max_length=10, unique=True)
    logo = models.ImageField(upload_to='empresas/images', null=True, blank=True)

    class Meta:
        ordering = ['sigla']

    def __str__(self):
        return self.sigla

class Regional(ControleTemporal):
    nome = models.CharField(max_length=50)
    slug = models.SlugField('Atalho', max_length=50)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Regionais'

    def __str__(self):
        return self.nome

class Agencia(ControleTemporal):
    empresa = models.ForeignKey(Empresa)
    regional = models.ForeignKey(Regional)
    nome = models.CharField(max_length=100)
    slug = models.SlugField('Atalho', max_length=100)
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES, default='AT')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Agência'
        verbose_name_plural = 'Agências'

    def __str__(self):
        return self.nome


