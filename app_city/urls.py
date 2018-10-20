from django.urls import path, include
from .views import pagina_inicial

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
]
