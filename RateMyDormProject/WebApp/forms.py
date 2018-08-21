from django import forms
from .models import Review, Dorm, College


# class ReviewForm(forms.ModelForm):
# 	class Meta:
# 		model = Review
# 		fields = ('college', 'dorm', 'description', 'year_lived', 'room_rating', 'bathroom_rating', 'dorm_rating')

# 		def __init__(self, *args, **kwargs):
# 			super().__init__(*args, **kwargs)
# 			qs = College.objects.none()
# 			self.fields['description']= 'test'
