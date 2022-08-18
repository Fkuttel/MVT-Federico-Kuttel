from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Te


# Create your views here.
class Creacion(CreateView):
    model=Te
    template_name = "Te/crearte.html"
    success_url = "/Infusiones/te"
    fields = ["nombre", "aroma"]
    
    
class ListadoTe(ListView):
      model=Te
      template_name = "Te/listado_tes.html"
      
      
class Editar(LoginRequiredMixin, UpdateView):
    model=Te
    template_name = "Te/editar_te.html"
    success_url = "/Infusiones/te"
    fields = ["nombre", "aroma"]
    
    
class Borrar(LoginRequiredMixin, DeleteView):
    model=Te
    template_name = "Te/eliminar.html"
    success_url = "/Infusiones/te"
    fields = ["nombre", "aroma"]
    