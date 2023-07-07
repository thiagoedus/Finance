from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('gerenciar/', views.gerenciar, name="gerenciar"),
    path('cadastrar_banco', views.cadastrar_banco, name="cadastrar_banco"),
    path('remover_banco/<int:id>', views.remover_banco, name="remover_banco"),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('deletar_categoria/<int:id>', views.deletar_categoria, name='deletar_categoria')
]