from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

def homepage(request):
 
 request.session['visitas'] = request.session.get('visitas', 0) + 1
 
 return render(request, 'home.html')

def registro(request):
    form = UserCreationForm(
        request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registro.html", {"form": form})

def logearse(request):
    form = AuthenticationForm(
        request,
        data=request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("/")
    return render(request, "login.html", {"form": form})
