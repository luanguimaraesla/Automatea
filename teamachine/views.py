from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import *

# Create your views here.
def index(request):
    user_list = Userdb.objects.all()
    template = loader.get_template('teamachine/index.html')
    context = RequestContext(request, {'user_list' : user_list,})
    return HttpResponse(template.render(context))

def home(request, user_id):
    return HttpResponse("HOME\n")

def create(request, user_id):
    return HttpResponse("Aqui cria-se chas!")

def order(request, user_id):
    return HttpResponse("Aqui se faz um pedido!")

def manage(request, user_id):
    return HttpResponse("Aqui se faz a manutencao do seu perfil")

def help(request, user_id):
    return HttpResponse("Aqui se pede ajuda e le as duvidas frequentes")

def login_verify(request):
    return HttpResponse("Aqui verifica-se o login")