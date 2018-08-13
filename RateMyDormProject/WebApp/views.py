from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'WebApp/home.html')

def about(request):
	return render(request, 'WebApp/about.html')

def schools(request):
	return render(request, 'WebApp/schools.html', {'content': ['Harvard', 'Yale', 'Kalamazoo']})

# Create your views here.
