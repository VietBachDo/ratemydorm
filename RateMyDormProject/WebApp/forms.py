from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)

