# Generated by Django 3.2.6 on 2021-09-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0012_alter_resumen_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='fecha',
            field=models.DateField(auto_now_add=True, verbose_name='fecha'),
        ),
    ]
