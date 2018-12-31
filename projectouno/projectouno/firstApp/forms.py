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
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        super(NewCourseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
