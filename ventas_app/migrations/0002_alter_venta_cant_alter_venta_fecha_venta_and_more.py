# Generated by Django 5.1 on 2024-12-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cant',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_venta',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]