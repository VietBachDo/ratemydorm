from django.db import models

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
	dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
	description = models.CharField(max_length=200,null=False)
	timestamp = models.DateTimeField(auto_now_add=True)