# Generated by Django 3.2.6 on 2021-09-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0011_auto_20210922_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='producto',
            field=models.CharField(max_length=200, verbose_name='producto'),
        ),
    ]
