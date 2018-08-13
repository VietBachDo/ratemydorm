from django.shortcuts import render
from django.http import HttpResponse
from .models import College, Dorm, Review
import xlrd

def homepage(request):
	return render(request, 'WebApp/home.html')

def about(request):
	return render(request, 'WebApp/about.html')

def schools(request):
	school_list = []

	for school in College.objects.all():
		school_list.append(school.name)
	
	context = {'Schools': sorted(school_list)}
	return render(request, 'WebApp/schools.html', context)


def addData(request):
	all_colleges = College.objects.all()


	# df = pd.read_excel("C:/Users/Zach/Desktop/projects/ratemydorm/list.xlsx","Sheet1")
	# college_names = df['Name'].values.tolist()
	# college_nicknames = df['Nicknames'].values.tolist()
	# index = 0
	# for name in college_names:
	# nicknames = college_nicknames[index]
	# index += 1

	# if not name in all_colleges:
	# 	entry = College(name=name, nicknames=nicknames)
	# 	entry.save()

	path = "C:/Users/Zach/Desktop/projects/ratemydorm/list.xlsx"

	wb = xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(0)

	for i in range(sheet.nrows):
		name = sheet.cell_value(i,0)
		if not name in all_colleges:
			nicknames = sheet.cell_value(i,1)
			entry = entry = College(name=name, nicknames=nicknames)
			entry.save()






	return render(request, 'WebApp/schools.html')
