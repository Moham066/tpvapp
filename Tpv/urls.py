"""Tpv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import include, path

import tpvapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/', include('tpvapp.urls')),
    path('add/', tpvapp.views.add_view),
    path('', include('django.contrib.auth.urls')),
    path('', tpvapp.views.login_view),
    path('singup/', tpvapp.views.singup_view),
    path('logout_user/', tpvapp.views.logout_view),
]
