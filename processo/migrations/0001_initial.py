# Generated by Django 3.0.8 on 2020-07-23 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('cliente', models.CharField(max_length=300, verbose_name='Cliente')),
                ('file', models.FileField(upload_to='', verbose_name='processos.csv')),
            ],
        ),
        migrations.CreateModel(
            name='processo',
            fields=[
                ('cadastro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='processo.cadastro')),
                ('pasta', models.CharField(max_length=10, verbose_name='Pasta')),
                ('comarca', models.CharField(max_length=200, verbose_name='Comarca')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
            bases=('processo.cadastro',),
        ),
    ]
