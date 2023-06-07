from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    return render(request, "page/homepage.html", {"platform": f"Araba: {randint(1, 10)}"})
