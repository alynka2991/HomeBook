# Generated by Django 3.1.6 on 2021-02-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='short_measure_name',
            field=models.CharField(blank=True, help_text='Короткое наименование единицы измерения', max_length=10, null=True, unique=True),
        ),
    ]