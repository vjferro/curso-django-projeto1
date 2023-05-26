from django.http import HttpResponse

#from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Home 3')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

