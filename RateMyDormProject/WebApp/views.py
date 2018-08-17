from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import College, Dorm, Review
from django.contrib.auth import authenticate, get_user_model, login, logout
import xlrd
import calendar;
import time;


#returns the homepage
def homepage(request):
	return render(request, 'WebApp/home.html')

#returns the 'about' page
def about(request):
	return render(request, 'WebApp/about.html')

#list all the schools
def listSchools(request):

	#list of dictionaries to store the school names and urls
	names_and_urls = []

	for school in College.objects.all():
		# name = school.name.replace(u'\xa0', u' ')
		dictionary = {}
		dictionary['name'] = school.name
		dictionary['url'] = school.url
		names_and_urls.append(dictionary)

	context = {'Schools': names_and_urls}


	return render(request, 'WebApp/schoolList.html', context)

#list all the dorms of that college
def schoolPage(request, school_url):

	#get the school name and its dorms
	school = College.objects.get(url__iexact=school_url)
	school_url = school.url
	dorm_list = Dorm.objects.filter(college__url=str(school_url))

	#send the list of dorms and the school name as context
	context = {'Dorms': dorm_list, 'School': school.name}

	return render(request, 'WebApp/school.html', context)

#
def dormPage(request, dorm_name):
	#get dorm object
	dorm = get_object_or_404(Dorm, name=dorm_name)

	#get reviews in reverse chronological order
	reviews = Review.objects.filter(dorm__name=dorm_name).order_by('-timestamp')

	#send the name of the dorm and its reviews as context
	context = {'Name': dorm, 'Reviews': reviews}
	
	return render(request, 'WebApp/dorm.html', context)


#add list of colleges to database
def addData(request):
	all_colleges = College.objects.all()

	path = "C:/Users/Zach/Desktop/projects/ratemydorm/list.xlsx"

	wb = xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(0)

	for i in range(sheet.nrows):
		name = sheet.cell_value(i,0)
		if not name in all_colleges:
			nicknames = sheet.cell_value(i,1)
			url = sheet.cell_value(i,2)
			entry = College(name=name, nicknames=nicknames, url=url)
			entry.save()

	return render(request, 'WebApp/schoolList.html')

#add dorms  from excel sheet to database
def addDorms(request):

	all_dorms = Dorm.objects.filter(college='Harvard University')

	path = "C:/Users/Zach/Desktop/projects/ratemydorm/dorms.xlsx"
	wb = xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(1)

	for i in range(sheet.nrows):
		name = sheet.cell_value(i,0)
		if not name in all_dorms:
			entry = Dorm(name=name, college='Harvard University')
			entry.save()

	return render(request, 'WebApp/schoolList.html')


class addReview(CreateView):
	model = Review
	fields = ['dorm', 'description', 'year_lived', 'room_rating', 'bathroom_rating', 'dorm_rating']
	
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(addReview, self).get_context_data(*args, **kwargs)
	# 	context['timestamp'] = calendar.timegm(time.gmtime())
	# 	return context