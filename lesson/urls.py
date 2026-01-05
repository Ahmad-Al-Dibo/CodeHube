from django.urls import path
from . import views


urlpatterns=[
    path("<int:lesson_id>", views.view_lesson, name="view_lesson"),
]