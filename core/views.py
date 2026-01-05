from django.shortcuts import render
from course.models import Course
from lesson.models import Lesson

# Create your views here.

def home(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all().order_by("-created_at")

    return render(request, "pages/home.html", context={
        "courses": courses,
        "lessons":lessons
    })


def about(request):
    return render(request, "pages/about.html", context={
        
    })