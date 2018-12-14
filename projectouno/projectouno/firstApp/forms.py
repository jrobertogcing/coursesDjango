from django import forms
from django.core import validators
from firstApp.models import Course


class CoursesForm(forms.Form):
    title = forms.CharField(max_length=255)
    # description = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)


class NewCourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = '__all__'

