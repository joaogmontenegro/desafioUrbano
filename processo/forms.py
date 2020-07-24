from django import forms
from .models import cadastro

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = ['file']