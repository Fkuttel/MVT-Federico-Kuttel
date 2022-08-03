from django.urls import path
from . import views

urlpatterns =    [
    path('crear/', views.Creacion.as_view() , name= "creacion"),
    path('te/',views.ListadoTe.as_view() , name= "listado_te"),
    path('editar/<int:pk>',views.Editar.as_view() , name= "editar"),
    path('borrar/<int:pk>', views.Borrar.as_view(), name= "borrar"),
                ]