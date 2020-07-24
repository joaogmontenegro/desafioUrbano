from django.db import models
import csv

class cadastro(models.Model):
    nome = models.CharField('Nome',max_length=300)
    cliente = models.CharField('Cliente', max_length=300)
    file = models.FileField('processos.csv',upload_to='processo')
    activated = models.BooleanField(default=False)
    def __str__(self):
        return f"File id{self.id}"

class processo(cadastro):
    pasta = models.CharField('Pasta',max_length=10)
    comarca = models.CharField('Comarca',max_length=200)
    uf = models.CharField('UF',max_length=2)


# Create your models here.
