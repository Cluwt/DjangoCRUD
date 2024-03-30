from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.app, name='app'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'), 
    path('excluir-usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('editar-usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
]
