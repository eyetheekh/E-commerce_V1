# Generated by Django 4.2.10 on 2024-04-21 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
