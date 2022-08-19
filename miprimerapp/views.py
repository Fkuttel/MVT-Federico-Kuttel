from unittest import result
from django.shortcuts import redirect, render

from .forms import BuscarCafe, FormCafe
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
    # if(request.method == "POST"):
    #     nombre = request.POST.get("nombre")
    #     tostado = request.POST.get("tostado")
    #     cuerpo = request.POST.get("cuerpo")
    #     cafe = Cafe(nombre=nombre, tostado=tostado, cuerpo=cuerpo)
    #     cafe.save()
    if request.method == "POST":
        form = FormCafe(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            cafe = Cafe(
                nombre=data.get("nombre"),
                tostado=data.get("tostado"),
                cuerpo=data.get("cuerpo"),
                descripcion=data.get("descripcion"),
                )
            cafe.save()
            listado_cafes = Cafe.objects.all()
            
            return render(request,"Cafe/listado_cafes.html", {"listado_cafes": listado_cafes})
        else:
            return render(request,"Cafe/crearcafes.html", {"form":form})
            
            
    form_cafe = FormCafe()
 
    return render(request,"Cafe/crearcafes.html", {"form":form_cafe})

def listado_cafes(request):
    resultado_busqueda = request.GET.get("nombre")
    
    if resultado_busqueda:
        listado_cafes = Cafe.objects.filter(nombre__icontains=resultado_busqueda) 
    else:
        listado_cafes = Cafe.objects.all()
    
    form =BuscarCafe()
            
    return render(request,"Cafe/listado_cafes.html", {"listado_cafes": listado_cafes, "form":form})

def acerca_de(request):
    return render (request, "about_us.html")

def editar_cafe(request,id):
    cafe = Cafe.objects.get(id=id)

    if request.method == "POST":
        form = FormCafe(request.POST)
        if form.is_valid():
            cafe.nombre = form.cleaned_data.get("nombre")
            cafe.tostado = form.cleaned_data.get("tostado")
            cafe.cuerpo = form.cleaned_data.get("cuerpo")
            cafe.descripcion = form.cleaned_data.get("descripcion")
            cafe.save()
            
            return redirect ("listado_cafes")
        else:
            return render(request,"Cafe/editar_cafe.html", {"form":form,"cafe":cafe})
 

    form_cafe = FormCafe(initial={"nombre":cafe.nombre,
                                  "tostado":cafe.tostado,
                                  "descripcion":cafe.descripcion,
                                  "cuerpo":cafe.cuerpo})
 
    return render(request,"Cafe/editar_cafe.html", {"form":form_cafe,"cafe":cafe})
            
            

def borrar_cafe(request,id):
    cafe = Cafe.objects.get(id=id)
    cafe.delete()
    
    return redirect ("listado_cafes")

def mostrar_cafe(request,id):
    cafe = Cafe.objects.get(id=id)
    return render (request, "Cafe/mostrar_cafe.html", {"cafe": cafe})