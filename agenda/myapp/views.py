from django.shortcuts import render, redirect
from myapp.models import Evento


def index(request):
    return redirect('/agenda/')



def listaEventos(request):

    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)

    dados = {'eventos': evento}


    return render(request, 'agenda.html', dados)






