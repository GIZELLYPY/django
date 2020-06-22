from django.db import models

# vamos relacionar o evento com o usuario logado da tabela do django
from django.contrib.auth.models import User


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Nome do Evento')
    descricao = models.TextField(blank=True, null=True, verbose_name= 'Descrição')
    data_evento = models.DateTimeField(verbose_name= 'Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name= 'Data de criação do evento')

    # vamos relacionar o evento com o usuario logado da tabela do django
    # on_delete=models.CASCADE() SE O USUARIO FOR EXCLUIDO, exclui tbm todos os eventos dele
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo # para aparecer o titulo do evento

    def converte_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Horas')
