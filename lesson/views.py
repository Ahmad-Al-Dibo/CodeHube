from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Lesson

def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {
        "lesson":lesson
    }
    return render(request, "lesson_view.html", context={
        **context
    })
