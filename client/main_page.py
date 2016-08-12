from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
import django.http
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def projects(request):
    return render(request, 'projects.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return django.http.HttpResponseRedirect('/admin/')
            else:
                return django.http.HttpResponse("Your account is disabled.")
        else:
            return django.http.HttpResponse("Wrong username and/or password.")

    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser

    return render(request, 'login.html', {})


@login_required(login_url='/login/')
def admin_panel(request):
    return render(request, 'admin.html', {})
