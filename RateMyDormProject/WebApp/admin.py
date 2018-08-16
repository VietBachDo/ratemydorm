from django.contrib import admin

from .models import Dorm, Review, College


#import models


class ReviewAdmin(admin.ModelAdmin):
	fields = [
		'dorm',
		'description',
		'timestamp',
	]
	readonly_fields = ['timestamp']


admin.site.register(College)
admin.site.register(Dorm)
admin.site.register(Review, ReviewAdmin)

