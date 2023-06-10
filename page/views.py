
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "page/homepage.html", {"platform": f"Araba: {randint(1, 10)}"})

def about(request):
    context=dict ()
    return render(request, "page/hakkimizda.html",context)

def contact(request):
    context=dict ()
    return render(request, "page/iletisim.html",context)

def vision(request):
    context=dict ()
    return render(request, "page/vizyonumuz.html",context)