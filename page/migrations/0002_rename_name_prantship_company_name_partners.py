# Generated by Django 4.2 on 2023-05-08 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name_prantship',
            new_name='name_partners',
        ),
    ]
