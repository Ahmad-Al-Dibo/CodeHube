from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        exclude = ("auther",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "icon": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'name': 'Course Name',
            'description': 'Course Description',
            'icon': 'Icon',
        }


