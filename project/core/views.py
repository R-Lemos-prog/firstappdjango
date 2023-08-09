from django.shortcuts import render
from project.modulos import facade


def home(request):
    return render(request, 'core/home.html')
