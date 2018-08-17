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
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    
    #domain.com/
    url(r'^$', views.homepage, name='homepage'),

    #domain.com/register
    url(r'^register/$', views.SignUp.as_view(), name='signup'),

    #domain.com/about/
    url(r'^about/$', views.about, name='about'),

    #domain.com/schools/
    url(r'^schools/$', views.listSchools, name='schools'),

    #domain.com/data/
    url(r'^data/$', views.addData, name='addData'),

    #domain.com/addDorms/
    url(r'^addDorms/$', views.addDorms, name='addDorms'),

    #domain.com/<SCHOOL_NAME>/
    url(r'^(?P<school_url>[\w, -]+)/$', views.schoolPage, name='schoolPage'),
    
    #domain.com/dorm/<DORM_NAME>
    url(r'^dorm/(?P<dorm_name>[\w, -]+)/$', views.dormPage, name='dormPage'),

    #domain.com/<SCHOOL_NAME>/AddReview
    url(r'^(?P<school_url>[\w, -]+)/AddReview/$', views.addReview.as_view(), name='add-review'),





]
