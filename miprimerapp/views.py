from django.http import HttpResponse

from django.template import loader

from miprimerapp.models import Familiares


def mi_template(request, nombre_familiar,edad_familiar):
    template1 = loader.get_template("prueba.html")
    # nombre = "jonas"
    familiares = Familiares(nombre=nombre_familiar, edad=edad_familiar,altura=150)
    familiares.save()
    lista_de_familia = Familiares.objects.all()
    
    render1 = template1.render({"lista_de_familia":lista_de_familia})

    # render1 = template1.render({"nombre":nombre})
    return HttpResponse(render1)