"""proje1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from page.views import about, adver, contact, home, vision

urlpatterns = [
    path('hakkimizda.html/', about, name = 'about_us'),
    path('ilan.html/', adver, name = 'advertorial'),
    path('iletisim.html/', contact, name = 'about_us'),
    path('homepage.html',home, name = 'home_1'),
    path('vizyonumuz.html/', vision, name = 'vision'),
    path('admin/', admin.site.urls),
]
