# Generated by Django 3.2.8 on 2021-12-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(auto_created=True),
        ),
    ]
