# Generated by Django 3.2.8 on 2021-12-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.CharField(max_length=30),
        ),
    ]