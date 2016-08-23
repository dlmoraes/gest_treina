# coding=utf-8

from django import forms
from cat.models import Pessoa
from .models import Matricula, Treinamento

class TreinamentoForm(forms.ModelForm):

    class Meta:
        model = Treinamento
        fields = '__all__'

class MatriculaInicialForm(forms.ModelForm):

    pessoa = forms.ModelChoiceField(queryset=Pessoa.objects.exclude(pessoa__matricula__isnull=False),
                                    required=True, label='Pessoa')

    class Meta:
        model = Matricula
        fields = ['pessoa']



class MatriculaRotinaForm(forms.ModelForm):

    pessoa = forms.ModelChoiceField(queryset=Pessoa.objects.filter(pessoa__matricula__isnull=False),
                                    required=True, label='Atendente')
    class Meta:
        model = Matricula
        fields = ['pessoa']

def get_ordereditem_formset(form, formset=forms.BaseInlineFormSet, **kwargs):
    return forms.inlineformset_factory(Treinamento, Matricula, form, formset, **kwargs)

class BaseMatriculaFormSet(forms.BaseModelFormSet):

    def clean(self):

        if any(self.errors):
            return

        pessoas = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                pessoa = form.cleaned_data['pessoa']

                if pessoa in pessoas:
                    duplicates = True
                pessoas.append(pessoa)

                if duplicates:
                    raise forms.ValidationError('Você selecionou a mesma pessoa/atendente, mais de uma vez.')

