# Generated by Django 3.2.7 on 2021-10-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='products',
            field=models.ManyToManyField(blank=True, to='Clientes.Products'),
        ),
    ]