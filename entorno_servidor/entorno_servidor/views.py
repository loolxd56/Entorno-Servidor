from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def homepage(request):
    request.session['visitas'] = request.session.get('visitas', 0) + 1
    return render(request, 'home.html')


def registro(request):
    request.session['visitas'] = request.session.get('visitas', 0) + 1
    form = UserCreationForm(
        request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registro.html", {"form": form})


def logearse(request):
    request.session['visitas'] = request.session.get('visitas', 0) + 1
    form = AuthenticationForm(
        request,
        data=request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("/")
    return render(request, "login.html", {"form": form})


@login_required
@permission_required("auth.delete_user", raise_exception=True)
def gestionar_usuarios(request):
    request.session['visitas'] = request.session.get('visitas', 0) + 1

    if request.method == "POST":
        usuario_id = request.POST.get("usuario_id")
        if usuario_id:
            User.objects.filter(id=usuario_id).delete()
            return redirect("gestionar_usuarios")

    usuarios = User.objects.all()
    return render(request, "gestionar.html", {"usuarios": usuarios})