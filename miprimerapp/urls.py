from .views import crear_cafe, mi_template,nuevo_index
from django.urls import path


urlpatterns = [

    path('', nuevo_index,name="index"),
    path('template/', mi_template, name= "cafeinomanos_only"),
    path('crear/', crear_cafe, name= "creacion"),

]