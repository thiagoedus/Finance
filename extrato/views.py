from django.shortcuts import render, redirect
from perfil.models import Conta, Categoria
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime


def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})

    elif request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta_usuario = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta_usuario,
            tipo=tipo,
        )

        valores.save()

        conta = Conta.objects.get(id=conta_usuario)

        if tipo == 'E':
            messages.add_message(request, constants.SUCCESS,
                                 'Entrada cadastrada com sucesso')
            conta.valor += int(valor)
        elif tipo == 'S':
            messages.add_message(request, constants.SUCCESS,
                                 'Saída cadastrada com sucesso')
            conta.valor -= int(valor)
        else:
            messages.add_message(request, constants.ERROR,
                                 'Ocorreu um erro inesperado')

        conta.save()

        return redirect('novo_valor')


def view_extrato(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()

        conta_get = request.GET.get('conta')
        categoria_get = request.GET.get('categoria')

        valores = Valores.objects.filter(data__month=datetime.now().month)
        return render(request, 'view_extrato.html', {'contas': contas, 'categorias': categorias, 'valores': valores})
