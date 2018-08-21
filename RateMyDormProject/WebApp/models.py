from django.db import models
from django.urls import reverse
from datetime import datetime as dt
from django.contrib.auth.models import User

#table for colleges
class College(models.Model):
	name = models.CharField(max_length=50)
	nicknames = models.CharField(max_length=50, blank=True)
	url = models.CharField(max_length=20, blank=False)

	#return name of college
	def __str__(self):
		return self.name


#table for dorms
class Dorm(models.Model):
	name = models.CharField(max_length=50)
	college = models.ForeignKey(College, on_delete=models.CASCADE)
	overall_rating = models.IntegerField(blank=False, default=1)

	#return name of dorm
	def __str__(self):
		return self.name


#table for reviews
class Review(models.Model):

	#list of rating choices (1-5)
	RATING_CHOICES = (
    	(1, '1'),
    	(2, '2'),
    	(3, '3'),
    	(4, '4'),
    	(5, '5'),
	)

	#create the list of year choices
	YEAR_CHOICES = []
	for i in range(1980, dt.now().year+1):
		YEAR_CHOICES.append((i,i))

	college = models.ForeignKey(College, on_delete=models.CASCADE)
	dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
	description = models.CharField(max_length=200,null=False)
	year_lived = models.IntegerField(choices=YEAR_CHOICES, default=dt.now().year)
	timestamp = models.DateTimeField(auto_now_add= True)
	room_rating = models.IntegerField(blank=False, choices=RATING_CHOICES, default=1)
	bathroom_rating = models.IntegerField(blank=False, choices=RATING_CHOICES, default=1)
	dorm_rating = models.IntegerField(blank=False, choices=RATING_CHOICES, default=1)
	likes = models.ManyToManyField(User, blank=True)

	#redirect here when Review object gets created
	def get_absolute_url(self):
		return reverse('dormPage', kwargs={'dorm_name':self.dorm})