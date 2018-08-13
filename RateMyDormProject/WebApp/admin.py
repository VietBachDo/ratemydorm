from django.contrib import admin

from .models import Dorm, Review, College


#import models
admin.site.register(Dorm)
admin.site.register(Review)
admin.site.register(College)
