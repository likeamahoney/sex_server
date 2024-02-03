from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm, EditForm

from .models import User, PsychoType

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
        user, created = User.objects.get_or_create(name = request.POST.get("name"))
        if not created:
            return HttpResponseRedirect("/?user_exist=True")
        ptypes = request.POST.getlist("psycho_types", [])
        user.save()
        
        for ptype in ptypes:
            pt, _ = PsychoType.objects.get_or_create(name = ptype)
            user.ptypes.add(pt)
        return HttpResponseRedirect(f"/?welcome=Добро пожаловать в семью {' и '.join(ptypes)}")

    form = EditForm() if request.GET.get("edit", False) else RegisterForm()
    return render(request, "register.html", { "form" : form })

def edit(request, name):
    try:
        if request.method == "POST":
            user = User.objects.get(name = name)
            ptypes = request.POST.getlist("psycho_types", [])
            user.save()
            user.ptypes.clear()

            for ptype in ptypes:
                pt, _ = PsychoType.objects.get_or_create(name = ptype)
                user.ptypes.add(pt)
            return HttpResponseRedirect("/?welcome=Съебал хуета")

        return HttpResponseRedirect("/register/?edit=True")
    except User.DoesNotExist:
        return HttpResponseRedirect("/?user_not_exist=True")

def delete(request, name):
    try:
        user = User.objects.get(name = name)
        user.delete()
        return redirect("index")
    except User.DoesNotExist:
        return HttpResponseRedirect("/?user_not_exist=True")
