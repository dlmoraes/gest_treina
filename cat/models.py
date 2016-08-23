# coding=utf-8
from django.db import models
from cag.models import Agencia
from core.lists import SITUACAO_CHOICES
from core.models import ControleTemporal

class Cargo(ControleTemporal):
    nome = models.CharField(max_length=50, unique=True, help_text='O nome do cargo deve ser único')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Pessoa(ControleTemporal):
    nome = models.CharField(max_length=100)
    dta_nascimento = models.DateField()
    doc_cpf = models.CharField('CPF', max_length=14, unique=True, help_text='Informe o CPF')
    doc_rg = models.CharField('RG', max_length=25, unique=True, help_text='Informe o RG, o registro informado deve ser único')
    avatar = models.ImageField(upload_to='pessoa/images', null=True, blank=True)

    def __str__(self):
        return self.nome

class Atendente(ControleTemporal):
    pessoa = models.OneToOneField(Pessoa, related_name='pessoa')
    matricula = models.CharField(max_length=15, help_text='A matricula deve ser única.')
    dta_entrevista = models.DateField('Data da entrevista', null=True, blank=True)
    dta_contratacao = models.DateField('Data da contratação', null=True, blank=True)
    dta_desligamento = models.DateField('Data do desligamento', null=True, blank=True)
    cargo = models.ForeignKey(Cargo, related_name='cargo')
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES, default='AT')
    agencia = models.ForeignKey(Agencia, related_name='agencia')

    def __str__(self):
        return self.pessoa.nome

