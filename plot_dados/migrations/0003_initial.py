# Generated by Django 4.0.5 on 2022-06-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plot_dados', '0002_delete_plot_dados'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseTeste',
            fields=[
                ('id_loja', models.IntegerField(primary_key=True, serialize=False)),
                ('id_area', models.IntegerField(blank=True, null=True)),
                ('tipo_compra', models.CharField(blank=True, max_length=10, null=True)),
                ('contagem_clientes_mes', models.IntegerField(blank=True, null=True)),
                ('total_vendas', models.IntegerField(blank=True, null=True)),
                ('mes_referencia', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
