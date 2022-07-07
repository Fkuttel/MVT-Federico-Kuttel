from django.shortcuts import render
from miprimerapp.models import Cafe


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