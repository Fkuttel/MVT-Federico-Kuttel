from .views import mi_template
from django.urls import path


urlpatterns = [

    path('template/<nombre_familiar>/<edad_familiar>', mi_template),
]