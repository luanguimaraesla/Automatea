from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from .models import *

# Create your views here.
def index(request):
    user_list = User.objects.all()
    template = loader.get_template('teamachine/index.html')
    context = RequestContext(request, {'user_list': user_list, })
    return HttpResponse(template.render(context))


def home(request, user_id):
    logged_user = User.objects.get(pk=user_id)
    template = loader.get_template('teamachine/home.html')
    context = RequestContext(request, {'logged_user' : logged_user, })
    return HttpResponse(template.render(context))


def create(request, user_id):
    return HttpResponse("Aqui cria-se chas!")


def order(request, user_id, tea_id):
    return HttpResponse("Aqui se faz um pedido!")


def manage(request, user_id):
    return HttpResponse("Aqui se faz a manutencao do seu perfil")


def help(request, user_id):
    return HttpResponse("Aqui se pede ajuda e le as duvidas frequentes")


def login_verify(request):
    return HttpResponse("Aqui verifica-se o login")


def singup(request):
    template = loader.get_template('teamachine/singup.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def register(request):
    c = {}
    c.update(csrf(request))

    if (request.POST['mail'] in [each_user.mail for each_user in User.objects.all()] or
                request.POST['nick'] in [each_user.nick_name for each_user in User.objects.all()]):
        template = loader.get_template('teamachine/singupfail.html')
        context = {}

    else:
        new_user = User(name=request.POST['name'],
                        nick_name=request.POST['nick'],
                        password=request.POST['password'],
                        photo_path=request.POST['photo'],
                        mail=request.POST['mail'])

        template = loader.get_template('teamachine/register.html')
        context = RequestContext(request, {"name": request.POST['name'],
                                           "nick": request.POST['nick'],
                                           "password": request.POST['password'],
                                           "mail": request.POST['mail'],
                                           "photo": request.POST['photo'],
                                           "user": new_user,
                                           })

    return HttpResponse(template.render(context))
