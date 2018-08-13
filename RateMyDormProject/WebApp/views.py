from django.shortcuts import render
from django.http import HttpResponse
from .models import College, Dorm, Review
import pandas as pd

def homepage(request):
	return render(request, 'WebApp/home.html')

def about(request):
	return render(request, 'WebApp/about.html')

def schools(request):
	all_dorms = Dorm.objects.all()
	school_list = []
	for dorm in all_dorms:
		if not dorm.college in school_list:
			school_list.append(dorm.college)
	
	context = {'Schools': school_list}
	return render(request, 'WebApp/schools.html', context)


def addData(request):
	all_colleges = College.objects.all()


	df = pd.read_excel("C:/Users/Zach/Desktop/projects/ratemydorm/list.xlsx","Sheet1")
	college_names = df['Name'].values.tolist()
	college_nicknames = df['Nicknames'].values.tolist()

	index = 0

	for name in college_names:
		nicknames = college_nicknames[index]
		index += 1

		if not name in all_colleges:
			entry = College(name=name, nicknames=nicknames)
			entry.save()

