from django.contrib import messages
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from encuestas.forms import EncuestaForm


def inicio(request):
    return render(request, 'encuestas/inicio.html')


class CreateEncuesta(CreateView):
    template_name = 'encuestas/create_encuesta.html'
    form_class = EncuestaForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, 'La encuesta se ha guardado satisfactoriamente.')
        return super(CreateEncuesta, self).form_valid(form)


