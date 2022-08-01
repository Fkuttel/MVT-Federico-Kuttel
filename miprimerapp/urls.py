from .views import acerca_de, crear_cafe, mi_template,nuevo_index,listado_cafes
from django.urls import path


urlpatterns = [

    path('', nuevo_index,name="index"),
    path('template/', mi_template, name= "cafeinomanos_only"),
    path('crear/', crear_cafe, name= "creacion"),
    path('cafes/', listado_cafes, name= "listado_cafes"),
    path('about_us/', acerca_de, name= "acerca_de"),

]