# Generated by Django 4.2.3 on 2023-07-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(default='Nova Categoria', max_length=50),
        ),
        migrations.AddField(
            model_name='categoria',
            name='essencial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='categoria',
            name='valor_planejamento',
            field=models.FloatField(default=0),
        ),
    ]