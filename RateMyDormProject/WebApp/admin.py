from django.contrib import admin

from .models import Dorm, Review


#import models
admin.site.register(Dorm)
admin.site.register(Review)
