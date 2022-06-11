from rest_framework import serializers
from plot_dados.models import DatabaseTeste


class DMS_1(serializers.ModelSerializer):   
    ticket_medio_por_cliente = serializers.SerializerMethodField()
    class Meta:
        model = DatabaseTeste
        fields = [
            'total_vendas',
            'contagem_clientes_mes',
            'ticket_medio_por_cliente',
            ]    
    def get_ticket_medio_por_cliente(self, obj):
        vendas_mes = int(obj.total_vendas)        
        clientes_mes = int(obj.contagem_clientes_mes)  
        total_mes = vendas_mes / clientes_mes      
        return round(total_mes, 2)


class DMS_2(serializers.ModelSerializer): 
    class Meta:
        model = DatabaseTeste
        fields = [
            'mes_referencia',
            'total_vendas',            
            ]


class DMS_3(serializers.ModelSerializer): 
    class Meta:
        model = DatabaseTeste
        fields = [
            'mes_referencia',
            'total_vendas',            
            'tipo_compra',
            ]     
