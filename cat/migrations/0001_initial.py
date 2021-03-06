# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cag', '0002_auto_20160818_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('matricula', models.CharField(help_text='A matricula deve ser única.', max_length=15, unique=True)),
                ('dta_entrevista', models.DateField(blank=True, null=True, verbose_name='Data da entrevista')),
                ('dta_contratacao', models.DateField(blank=True, null=True, verbose_name='Data da contratação')),
                ('dta_desligamento', models.DateField(blank=True, null=True, verbose_name='Data do desligamento')),
                ('situacao', models.CharField(choices=[('AT', 'Ativo'), ('IN', 'Inativo')], default='AT', max_length=2, verbose_name='Situação')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agencia', to='cag.Agencia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(help_text='O nome do cargo deve ser único', max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=100)),
                ('dta_nascimento', models.DateField()),
                ('doc_cpf', models.CharField(help_text='Informe o CPF', max_length=14, unique=True, verbose_name='CPF')),
                ('doc_rg', models.CharField(help_text='Informe o RG, o registro informado deve ser único', max_length=25, unique=True, verbose_name='RG')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='pessoa/images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='atendente',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='cat.Cargo'),
        ),
        migrations.AddField(
            model_name='atendente',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cat.Pessoa'),
        ),
    ]
