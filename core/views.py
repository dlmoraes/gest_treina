# coding=utf-8

from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()
