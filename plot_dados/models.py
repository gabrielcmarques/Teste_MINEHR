from django.db import models


class DatabaseTeste(models.Model):
    id_loja = models.IntegerField(primary_key=True)
    id_area = models.IntegerField(blank=True, null=True)
    tipo_compra = models.CharField(blank=True, null=True, max_length=10)
    contagem_clientes_mes = models.IntegerField(blank=True, null=True)
    total_vendas = models.IntegerField(blank=True, null=True)
    mes_referencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_teste'