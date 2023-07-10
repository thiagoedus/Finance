from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcula_total


def home(request):
    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')
    return render(request, "home.html", {'contas': contas, 'total_contas': total_contas})


def gerenciar(request):
    categorias = Categoria.objects.all()
    contas = Conta.objects.all()
    total_contas = 0
    for conta in contas:
        total_contas += conta.valor
    return render(request, "gerenciar.html", {'contas': contas, 'total': total_contas, 'categorias': categorias})


def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR,
                             'Preencha todos os campos')
        return redirect("gerenciar")

    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()
    messages.add_message(request, constants.SUCCESS,
                         'Os dados foram salvos com sucesso')
    return redirect('gerenciar')


def remover_banco(request, id):
    conta = Conta.objects.filter(id=id)
    conta.delete()
    messages.add_message(request, constants.SUCCESS,
                         'Conta deletada com sucesso')
    return redirect('gerenciar')


def cadastrar_categoria(request):
    categoria = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))
    valor_planejamento = request.POST.get('valor_planejamento')

    categoria = Categoria(
        categoria=categoria,
        essencial=essencial,
        valor_planejamento=valor_planejamento
    )

    categoria.save()
    messages.add_message(request, constants.SUCCESS,
                         'Categoria adicionada com sucesso')
    return redirect('gerenciar')


def deletar_categoria(request, id):
    categoria = Categoria.objects.filter(id=id)
    categoria.delete()
    messages.add_message(request, constants.SUCCESS,
                         'Categoria deletada com sucesso')
    return redirect('gerenciar')


def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    try:
        categoria.essencial = not categoria.essencial
        categoria.save()
        messages.add_message(request, constants.SUCCESS,
                             'Categoria alterada com sucesso')
    except:
        messages.add_message(request, constants.ERROR, 'Ocorreu um erro')
    return redirect('gerenciar')
