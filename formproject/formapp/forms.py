from django import forms

class StudentRegistration(forms.Form):
	Name = forms.charField()
	Marks = forms.IntegerField()