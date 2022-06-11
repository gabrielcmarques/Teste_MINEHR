from django.urls import path
from . import views

urlpatterns = [
    path('', views.rotas),
    path('primeiro/', views.vendas_clientes_ticket_medio, name='primeiro'),
    path('segundo/', views.vendas_mes, name='segundo'),
    path('terceiro/', views.vendas_presencial_online, name='terceiro'),
]