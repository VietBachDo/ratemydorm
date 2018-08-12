from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'WebApp/home.html')

def about(request):
	return render(request, 'WebApp/about.html')

# Create your views here.
