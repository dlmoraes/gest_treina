# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, verbose_name='Atalho')),
                ('situacao', models.CharField(choices=[('AT', 'Ativo'), ('IN', 'Inativo')], default='AT', max_length=2, verbose_name='Situação')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.SlugField(max_length=10, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='empresas/images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=50)),
                ('slug', models.SlugField(verbose_name='Atalho')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='agencia',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cag.Empresa'),
        ),
        migrations.AddField(
            model_name='agencia',
            name='regional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cag.Regional'),
        ),
    ]
