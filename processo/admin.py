from django.contrib import admin
from .models import cadastro, processo



@admin.register(processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('pasta', 'comarca', 'uf')

# Register your models here.
