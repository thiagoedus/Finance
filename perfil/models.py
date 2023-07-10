from django.db import models
from datetime import datetime


class Categoria(models.Model):
    categoria = models.CharField(max_length=50, default='Nova Categoria')
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria

    def total_gasto(self):
        from extrato.models import Valores
        from perfil.utils import calcula_total
        valores = Valores.objects.filter(categoria__id=self.id).filter(
            data__month=datetime.now().month).filter(tipo='S')
        total_gasto = calcula_total(valores, 'valor')
        return total_gasto

    def calcula_percentual_gasto_por_categoria(self):
        return int((100*self.total_gasto()) / self.valor_planejamento)


class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Econômica'),
        ('BD', 'Bradesco'),
        ('BD', 'Bradesco'),
        ('IT', 'Itaú'),
    )

    tipo_choices = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    icone = models.ImageField(upload_to="icones")
    valor = models.FloatField(default=0)

    def __str__(self):
        return self.apelido
