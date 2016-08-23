# coding=utf-8

from django.contrib import messages
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, RedirectView, CreateView
from django.shortcuts import get_object_or_404, redirect, render_to_response
from cat.models import Pessoa
from .forms import *
from .models import Treinamento, Matricula

class TreinamentoList(ListView):

    template_name = 'ctr/treinamento/treinamentos.html'
    model = Treinamento
    context_object_name = 'treinamentos'


class MatriculaView(TemplateView):

    template_name = 'ctr/matricula/efetuar_matricula_new.html'

    def get_context_data(self, **kwargs):
        treinamento = get_object_or_404(Treinamento, id=self.kwargs['pk_treinamento'])
        context = super(MatriculaView, self).get_context_data(**kwargs)
        MatriculaFormSet = get_ordereditem_formset(MatriculaInicialForm, extra=1, can_delete=True)
        # MatriculaFormSet = get_ordereditem_formset(MatriculaRotinaForm, extra=1, can_delete=True)
        context['treinamento'] = treinamento
        context['form'] = TreinamentoForm(instance=treinamento)
        context['formset'] = MatriculaFormSet(instance=treinamento)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        treinamento = context['treinamento']
        if treinamento.tipo == 'inicial':
            MatriculaFormSet = get_ordereditem_formset(MatriculaInicialForm, extra=1, can_delete=True)
        else:
            MatriculaFormSet = get_ordereditem_formset(MatriculaRotinaForm, extra=1, can_delete=True)
        formset = MatriculaFormSet
        #if formset.is_valid():
        #    formset.save()
        #    messages.success(request, 'Matriculas efetuadas com sucesso!')
        #    return reverse_lazy('ctr:treinamentos')
        return self.render_to_response(context)


treinamentos = TreinamentoList.as_view()
efetuar_matricula = MatriculaView.as_view()

'''    def get_context_data(self, **kwargs):
        treinamento = get_object_or_404(Treinamento, id=self.kwargs['pk_treinamento'])
        context = super(MatriculaView, self).get_context_data(**kwargs)
        if treinamento.tipo == 'inicial':
            MatriculaInlineFormSet = inlineformset_factory(Treinamento,
                                                           Matricula,
                                                           form=MatriculaInicialForm,
                                                           extra=3,
                                                           max_num=10,
                                                           can_delete=False)

        else:
            MatriculaInlineFormSet = inlineformset_factory(Treinamento, Matricula, form=MatriculaRotinaForm, extra=3, max_num=10,
                                                           can_delete=False)
        context['formset'] = MatriculaInlineFormSet(instance=treinamento)
        return context
'''
