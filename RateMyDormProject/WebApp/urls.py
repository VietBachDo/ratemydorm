"""RateMyDormProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^schools/$', views.listSchools, name='schools'),
    url(r'^data/$', views.addData, name='addData'),
    url(r'^(?P<school_name>[\w, -]+$)', views.schoolPage, name='schoolPage'),
    url(r'^dorm/(?P<dorm_name>[\w, -]+)', views.dormPage, name='dormPage'),

]
