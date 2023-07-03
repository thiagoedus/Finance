from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    return render(request, "home.html")

def gerenciar(request):
    return render(request, "gerenciar.html")

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('apelido')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect("gerenciar")

    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        icone = icone
    )

    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Os dados foram salvos com sucesso')
    return redirect('gerenciar')