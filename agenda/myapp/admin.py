from django.contrib import admin
from myapp.models import Evento

# Register your models here.

class listaEvento(admin.ModelAdmin):
    list_display = ['titulo','descricao', 'data_evento', 'data_criacao','id']
    list_filter = ['titulo','data_evento']




admin.site.register(Evento,listaEvento)


