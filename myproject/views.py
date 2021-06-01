from django.http import HttpResponse
from django.http import render

def registration(request):
    return HttpResponse("<h1>Welcome to registration</h1>")