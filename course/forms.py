from django import forms
from lesson.models import Lesson
from course.models import Course

class LessonForm(forms.ModelForm):

    

    class Meta:
        model = Lesson
        fields = ("title", "course", "slug", "content", "thumbnail")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "course": forms.Select(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "thumbnail": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'course': 'Course',
            'title': 'Lesson Title',
            'slug': 'Slug',
            'content': 'Lesson Content',
            'thumbnail': 'Thumbnail',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        print(user)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields["course"].queryset = Course.objects.filter(auther=user)
