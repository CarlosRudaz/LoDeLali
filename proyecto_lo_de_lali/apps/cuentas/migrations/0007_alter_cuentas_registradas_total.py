# Generated by Django 3.2.6 on 2021-09-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_auto_20210922_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas_registradas',
            name='total',
            field=models.FloatField(default=0, null=True, verbose_name='total'),
        ),
    ]
