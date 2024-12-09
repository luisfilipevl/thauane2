from django.urls import path
from .views import *

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    # Add your URL patterns here
    path('Voos/', listagem_Voo, name='listagem_Voo'),
    path('Voos/cadastro', cadastrar_Voo, name='cadastro_Voo'),
    path('Voos/editar/<int:id>', editar_Voo, name='editar_Voo'),
    path('Voos/excluir/<int:id>', excluir_Voo, name='excluir_Voo'),
]