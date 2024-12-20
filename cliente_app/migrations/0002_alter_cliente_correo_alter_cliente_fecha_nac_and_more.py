# Generated by Django 5.1 on 2024-12-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nac',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.PositiveIntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
