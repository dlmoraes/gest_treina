from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from .models import Cargo, Pessoa, Atendente

class CargoCreate(CreateView):

    template_name = 'cat/cargo/cargo_add.html'
    model = Cargo
    fields = '__all__'
    success_url = reverse_lazy('cat:cargos')

class CargoList(ListView):

    template_name = 'cat/cargo/cargos.html'
    model = Cargo
    paginate_by = 10
    context_object_name = 'cargos'

class PessoaList(ListView):

    template_name = 'cat/pessoa/pessoas.html'
    model = Pessoa
    paginate_by = 10
    context_object_name = 'pessoas'

class AtendenteList(ListView):

    template_name = 'cat/atendente/atendentes.html'
    model = Atendente
    paginate_by = 10
    context_object_name = 'atendentes'


# Creates
add_cargo = CargoCreate.as_view()

# Lists
cargos = CargoList.as_view()
pessoas = PessoaList.as_view()
atendentes = AtendenteList.as_view()