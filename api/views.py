from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from plot_dados.models import DatabaseTeste
from .serializers import DMS_1, DMS_2, DMS_3

# url/api #
@api_view(['GET'])
def rotas(request):
    rotas = [
        {'1: Retornar 3 indicadores:': '/api/primeiro'},
        {'2: Total vendido por mês': '/api/segundo'},
        {'3: Total vendido por tipo de compra por mês (Presencial ou Online)': '/api/terceiro'},
    ]
    return Response(rotas)

# url/api/primeiro #
@api_view(['GET'])
def vendas_clientes_ticket_medio(request):
    dados = DatabaseTeste.objects.all()        
    serializer = DMS_1(dados, many=True)
    return Response(serializer.data)

# url/api/segundo #
@api_view(['GET'])
def vendas_mes(request):
    dados = DatabaseTeste.objects.all()        
    serializer = DMS_2(dados, many=True)
    return Response(serializer.data)

# url/api/terceiro #
@api_view(['GET'])
def vendas_presencial_online(request):
    dados = DatabaseTeste.objects.all()        
    serializer = DMS_3(dados, many=True)
    return Response(serializer.data)
