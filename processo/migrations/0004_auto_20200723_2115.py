# Generated by Django 3.0.8 on 2020-07-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0003_auto_20200723_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='file',
            field=models.FileField(upload_to='processos', verbose_name='processos.csv'),
        ),
    ]
