from django.db import models
from django.urls import reverse
from datetime import datetime as dt

#table for colleges
class College(models.Model):
	name = models.CharField(max_length=50, blank=False)
	nicknames = models.CharField(max_length=50, blank=True)
	url = models.CharField(max_length=20, blank=False)

	#return name of college
	def __str__(self):
		return self.name


#table for dorms
class Dorm(models.Model):
	name = models.CharField(max_length=50, blank=False)
	college = models.ForeignKey(College, on_delete=models.CASCADE)

	#return name of dorm
	def __str__(self):
		return self.name


#table for reviews
class Review(models.Model):

	YEAR_CHOICES = []

	#create the list of year choices
	for i in range(1980, dt.now().year+1):
		YEAR_CHOICES.append((i,i))

	dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
	description = models.CharField(max_length=200,null=False)
	year_lived = models.IntegerField(choices=YEAR_CHOICES, default=dt.now().year)
	timestamp = models.DateTimeField(auto_now_add= True)

	#redirect here when Review object gets created
	def get_absolute_url(self):
		return reverse('dormPage', kwargs={'dorm_name':self.dorm})