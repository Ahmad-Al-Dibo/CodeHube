from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Lesson

def view_lesson(request, course_slug, lesson_slug ):
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course__slug = course_slug) 
    # lesson returns a Lesson object or a 404 error if not found
    context = {
        "lesson":lesson
    }
    return render(request, "lesson_view.html", context={
        **context
    })
