from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import College, Dorm, Review
import xlrd

def homepage(request):
	return render(request, 'WebApp/home.html')

def about(request):
	return render(request, 'WebApp/about.html')

#list all the schools
def listSchools(request):
	school_list = []

	for school in College.objects.all():
		name = school.name.replace(u'\xa0', u' ')
		school_list.append(name)
	
	context = {'Schools': sorted(school_list)}
	return render(request, 'WebApp/schoolList.html', context)

#list all the dorms of that college
def schoolPage(request, school_name):
	dorm_list = Dorm.objects.filter(college__name=str(school_name))
	context = {'Dorms': dorm_list, 'School': school_name}
	return render(request, 'WebApp/school.html', context)

#
def dormPage(request, dorm_name):
	dorm = get_object_or_404(Dorm, name=dorm_name)
	context = {'Name': dorm}
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
			entry = entry = College(name=name, nicknames=nicknames)
			entry.save()

	return render(request, 'WebApp/schoolList.html')


