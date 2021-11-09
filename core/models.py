from django.db import models
from django.db.models.fields import CharField, DecimalField

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome
