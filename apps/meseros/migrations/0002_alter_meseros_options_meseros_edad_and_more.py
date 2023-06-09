# Generated by Django 4.1.7 on 2023-03-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meseros',
            options={'verbose_name_plural': 'Meseros'},
        ),
        migrations.AddField(
            model_name='meseros',
            name='edad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meseros',
            name='procedencia',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='meseros',
            name='apellido',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='meseros',
            name='nombre',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
