from .views import mi_template,nuevo_index
from django.urls import path


urlpatterns = [

    path('', nuevo_index,name="index"),
    path('template/', mi_template, name= "cafeinomanos_only"),

]