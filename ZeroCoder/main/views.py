from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {"caption": "Django"}
    return render(request, "main/index.html", data)

def new(request):
    return render(request, "main/new.html")

def data(request):
    return HttpResponse("<h1>Это третья страница моего проекта на Django</h1>")

def test(request):
    return HttpResponse("<h1>Это четвертая страница моего проекта на Django</h1>")