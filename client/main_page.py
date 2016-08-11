from django.shortcuts import render
from django.template import loader, Context


def index(request):
    return render(request, 'home.html')
