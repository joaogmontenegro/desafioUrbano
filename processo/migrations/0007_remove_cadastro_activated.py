# Generated by Django 3.0.8 on 2020-07-24 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0006_auto_20200723_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='activated',
        ),
    ]
