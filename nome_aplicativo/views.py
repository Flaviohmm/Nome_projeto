from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registrar(request):
    form = CustomUserCreationForm()
    return render(request, 'nome_aplicativo/registrar.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
    else:
        form = CustomUserCreationForm()
    return render(request, 'nome_aplicativo/registrar.html', {'form': form})
