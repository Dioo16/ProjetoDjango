# Generated by Django 3.2.6 on 2021-09-03 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_auto_20210901_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_photos'),
        ),
    ]
