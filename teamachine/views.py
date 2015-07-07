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
    logged_user = User.objects.get(pk=user_id)
    template = loader.get_template('teamachine/create.html')
    taste_list = Teataste.objects.all()
    context = RequestContext(request, {'logged_user': logged_user,
                                       'taste_list' : taste_list,
                                       })

    return HttpResponse(template.render(context))


def order(request, user_id):
    c = {}
    c.update(csrf(request))

    selected_tea = Tea.objects.get(pk = request.POST["tea"])
    logged_user = User.objects.get(pk=user_id)

    template = loader.get_template('teamachine/order.html')
    context = RequestContext(request, {'logged_user' : logged_user,
                                       'selected_tea' : selected_tea,
                                       })

    return HttpResponse(template.render(context))


def manage(request, user_id):
    return HttpResponse("Aqui se faz a manutencao do seu perfil")


def help(request, user_id):
    return HttpResponse("Aqui se pede ajuda e le as duvidas frequentes")


def tearegister(request, user_id):
    logged_user = User.objects.get(pk = user_id)
    id_taste_list = request.POST.getlist('checks')
    name = request.POST['name']
    water_ml = request.POST['water_ml']
    taste_list = []
    for each_taste_id in id_taste_list:
        taste_list.append(Teataste.objects.get(pk = each_taste_id))

    logged_user.create_tea(name = name, taste = taste_list, water = water_ml, sugar = 0)

    template = loader.get_template('teamachine/tearegister.html')
    context = RequestContext(request, {'logged_user' : logged_user, })

    return HttpResponse(template.render(context))


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
        new_user.save()

        template = loader.get_template('teamachine/register.html')
        context = RequestContext(request, {"name": request.POST['name'],
                                           "nick": request.POST['nick'],
                                           "password": request.POST['password'],
                                           "mail": request.POST['mail'],
                                           "photo": request.POST['photo'],
                                           "new_user": new_user,
                                           })

    return HttpResponse(template.render(context))
