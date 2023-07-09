from django.shortcuts import render, redirect
from perfil.models import Conta, Categoria
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime
from django.template.loader import render_to_string
from django.conf import settings
import os
from django.http import HttpResponse, FileResponse
from weasyprint import HTML
from io import BytesIO

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

        if conta_get:
            valores = valores.filter(conta__id=conta_get)

        if categoria_get:
            valores = valores.filter(categoria_id=categoria_get)

        #TODO Botão de zerar filtros
        #TODO Filtrar por período

        return render(request, 'view_extrato.html', {'contas': contas, 'categorias': categorias, 'valores': valores})
    
def exportar_pdf(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)
    
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/extrato.html')
    template_render = render_to_string(path_template, {'valores':valores})
    
    path_output = BytesIO()
    HTML(string=template_render).write_pdf(path_output)
    path_output.seek(0)
    
    return FileResponse(path_output, filename="extrato.pdf")