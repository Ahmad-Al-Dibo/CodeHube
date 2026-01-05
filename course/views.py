from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Course
from lesson.models import Lesson

# Create your views here.

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)
    if course:
        return render(request, "dashboard/course.html", context={
            "course": course,
            "lessons": lessons
        })
    
    messages.error("here is no such course.")
    return redirect("index")