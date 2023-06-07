from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    return render(request, "page/homepage.html", {"platform": f"Araba: {randint(1, 10)}"})


def about(request):
    context=dict ()
    return render(request, "page/hakkimizda.html",context)

def contact(request):
    context=dict ()
    return render(request, "page/iletisim.html",context)