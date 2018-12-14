from django import forms

class CoursesForm(forms.Form):
    title = forms.CharField(max_length=255)
    # description = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)



