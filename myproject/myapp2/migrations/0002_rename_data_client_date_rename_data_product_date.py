# Generated by Django 4.2.11 on 2024-04-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='data',
            new_name='date',
        ),
    ]
