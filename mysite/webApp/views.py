from django.shortcuts import render, HttpResponse



def hello(request, nome, idade ):
    return HttpResponse('Hello {}, você tem {} anos de idade'.format(nome,idade))


