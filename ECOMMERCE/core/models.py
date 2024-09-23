from django.db import models
from stdimage.models import StdImageField

class Produto(models.Model):
    codigo = models.IntegerField('Código do Produto',blank=False, primary_key = True, unique= True, auto_created=True)#colunas
    nome = models.CharField('Nome do Produto',blank = False, max_length=100,)
    descricao = models.CharField('Descrição', max_length=100, blank=False)
    quantidade = models.IntegerField('Quantidade de Produto', blank=False)
    valor = models.DecimalField('Valor do produto',max_digits=10, decimal_places=2)
    imagem = StdImageField('Imagem do produto',blank=False,variations={'thumb':(124,124)})

    def __str__(self):
        return self.nome
#usuario aluno, senha: 99823580