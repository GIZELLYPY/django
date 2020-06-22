from django.shortcuts import render, redirect
from myapp.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request,usuario)
            return redirect('/')

        else:
            messages.error(request, "Usuário ou senha incorretos")

    return  redirect('/')


@login_required(login_url='/login/') # redireciona se não esta autenticado
def listaEventos(request):

    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)

    dados = {'eventos': evento}


    return render(request, 'agenda.html', dados)






