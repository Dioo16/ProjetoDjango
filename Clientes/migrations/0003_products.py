# Generated by Django 3.2.7 on 2021-10-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_sell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descrition', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
