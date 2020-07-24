from django.shortcuts import render
from django.contrib import messages
from .forms import CadastroModelForm
from django.http import HttpResponse
from .forms import CadastroModelForm

def index(request):
    return render(request,'index.html')

def upload_file_view(request):
    form = CadastroModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CadastroModelForm()
    return render(request,'upload.html',{'form':form})

def cadastro(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f'nome: {prod.nome}')
            print(f'cliente: {prod.cliente}')
            print(f'file: {prod.file}')
            messages.success(request,'Cadastro Realizado')
        else:
            messages.error(request,'Cadastro não realizado')
    else:
        form = CadastroModelForm()
    context = {
    'form':form
    }
    return render(request,'cadastro.html',context)

# Create your views here.
