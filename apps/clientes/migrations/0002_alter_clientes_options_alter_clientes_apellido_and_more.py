# Generated by Django 4.1.7 on 2023-03-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='clientes',
            name='apellido',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
