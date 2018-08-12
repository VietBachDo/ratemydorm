from django.db import models

#table for dorms
class Dorm(models.Model):
	name = models.CharField(max_length=50, blank=False)
	college = models.CharField(max_length=50, blank=False)


#table for reviews
class Review(models.Model):
	dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
	description = models.CharField(max_length=200,null=False)