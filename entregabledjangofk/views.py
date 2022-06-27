from django.http import HttpResponse
from datetime import datetime

from django.template import Context, Template


def inicio(request):
  return HttpResponse("jonas la tenes adentro")

def fecha_actual(request):
    fecha_de_hoy = datetime.today()
    return HttpResponse(f"jonas la tiene adentro en: {fecha_de_hoy}")

def saluditos(request,nombre, apellido):
    return HttpResponse(f"el que se la lastra se llama: {nombre} {apellido}")

def mi_template(request):
    archivo = open(r"C:\Users\Ale\Desktop\python fede\entregabledjango\templates\prueba.html", "r")
    template1 = Template(archivo.read())
    contexto1 = Context()
    render1 = template1.render(contexto1)
    return HttpResponse(render1)