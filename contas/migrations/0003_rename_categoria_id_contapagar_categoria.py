# Generated by Django 4.2.3 on 2023-07-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_rename_categoria_contapagar_categoria_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contapagar',
            old_name='categoria_id',
            new_name='categoria',
        ),
    ]
