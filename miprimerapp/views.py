from django.shortcuts import render
from .models import Cafe


def mi_template(request):
    cafe1 = Cafe(nombre ="Sumatra" )
    cafe2 = Cafe(nombre ="Etiopia" )
    cafe3 = Cafe(nombre ="Colombia" )
    cafe1.save()
    cafe2.save()
    cafe3.save()
    return render(request,"prueba.html", {"lista_de_cafe":[cafe1, cafe2, cafe3]})

def nuevo_index(request):
    
    return render (request,"index.html")

def crear_cafe(request):
    nombre = request.GET.get("nombre")
    tostado = request.GET.get("tostado")
    #cuerpo = request.GET.get("cuerpo")
    cafe = Cafe(nombre=nombre, tostado=tostado)
    #cafe.save()
 
    return render(request,"crearcafes.html",{"cafe":cafe})