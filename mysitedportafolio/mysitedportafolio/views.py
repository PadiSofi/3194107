from django.http import HttpResponse

from django.shortcuts import render, redirect

USUARIO = "sofia"
PASSWORD = "1234"

def login_view(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")

        if user == USUARIO and password == PASSWORD:
            request.session["logueado"] = True
            return redirect("inicio")
        else:
            return render(request, "cv_app/login.html", {"error": "Datos incorrectos"})

    return render(request, "cv_app/login.html")


def inicio(request):
    if not request.session.get("logueado"):
        return redirect("login")
    return render(request, "cv_app/inicio.html")


def quien_soy(request):
    if not request.session.get("logueado"):
        return redirect("login")
    return render(request, "cv_app/quien_soy.html")


def hobbies(request):
    if not request.session.get("logueado"):
        return redirect("login")
    return render(request, "cv_app/hobbies.html")


def experiencias(request):
    if not request.session.get("logueado"):
        return redirect("login")
    return render(request, "cv_app/experiencias.html")