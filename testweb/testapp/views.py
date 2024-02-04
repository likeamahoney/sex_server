from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm  #, EditForm

from .models import User, PsychoType

import logging

log = logging.getLogger(__name__)

def index(request):#, user_exist = False, user_not_exist = False, welcome = ""):
    #host = request.META["HTTP_HOST"] # получаем адрес сервера
    #user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    #path = request.path     # получаем запрошенный путь
     
    #return HttpResponse(f"""
    #    <p>Host: {host}</p>
    #    <p>Path: {path}</p>
    #    <p>User-agent: {user_agent}</p>
    #""")
    users = User.objects.all()
    return render(request, "index.html", context = { "users" : users, "user_exist" :  request.GET.get("user_exist", False), "user_not_exist" :  request.GET.get("user_not_exist", False), "welcome" :  request.GET.get("welcome", "")})

def user(request):
    name = request.GET.get("name", "Johnny Sins")
    #return HttpResponse(f"""
    #    <p><h1> Poshel Naxui: {name} </p></h1>
    #""")
    return render(request, "index_old.html", context={"name": name, })

def about(request):
    return HttpResponse("<p><h2>BRAZZERS INC.</h2></p>")

def register(request):
    #return render(request, "roulette.html")
    if request.method == "POST":
        edit = request.POST.get("edit", False)
        name = request.POST.get("name")
        user, created = User.objects.get_or_create(name = name)
        if not edit and not created:
            log.error(f"Failed to create user: User - {name} exist")
            return HttpResponseRedirect("/?user_exist=True")
        ptypes = request.POST.getlist("psycho_types", [])

        user.ptypes.clear()
        for ptype in ptypes:
            pt, _ = PsychoType.objects.get_or_create(name = ptype)
            user.ptypes.add(pt)
            pt.save()

        user.save()
        if not edit:
            log.debug(f"User - {name} created")
            return HttpResponseRedirect(f"/?welcome=Добро пожаловать в семью {' и '.join(ptypes)}")
        else:
            log.debug(f"User - {name} edited")
            return HttpResponseRedirect("/?welcome=Съебал хуета")

    if request.GET.get("edit", False):
      name = request.GET.get("name")
      form = RegisterForm(name = name)
      return render(request, "register.html", { "form" : form, "name" : name, "edit" : True})
    else:
      form = RegisterForm()
      return render(request, "register.html", { "form" : form})

def edit(request, name):
    #try:
    #    if request.method == "POST":
    #        user = User.objects.get(name = name)
    #        ptypes = request.POST.getlist("psycho_types", [])
    #        user.ptypes.clear()

    #        for ptype in ptypes:
    #            pt, created = PsychoType.objects.get_or_create(name = ptype)
    #            if created:
    #                pt.save()
    #            user.ptypes.add(pt)

    #        user.save(update_fields=["ptypes"])
    #        return HttpResponseRedirect("/?welcome=Съебал хуета")

    return HttpResponseRedirect(f'/register/?edit=True&name={name}')
    #except User.DoesNotExist:
    #    return HttpResponseRedirect("/?user_not_exist=True")

def delete(request, name):
    try:
        user = User.objects.get(name = name)
        user.delete()
        log.debug(f"User - {name} deleted")
        return redirect("index")
    except User.DoesNotExist:
        log.error(f"Failed to delete user: User - {name} does't exist")
        return HttpResponseRedirect("/?user_not_exist=True")
