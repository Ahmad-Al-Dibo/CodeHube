from django.urls import path
from . import views


urlpatterns=[
    path("<slug:course_slug>/<slug:lesson_slug>", views.view_lesson, name="view_lesson"),
]