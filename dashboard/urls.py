from django.urls import path
from . import views

urlpatterns=[
    path("", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("new_lesson/", views.new_lesson, name="new_lesson"),
    path("new_course/", views.new_course, name="new_course"),
    path("user_lessons/", views.user_lessons, name="user_lessons"),
    path("update_lesson/<int:lesson_id>", views.update_lesson, name="update_lesson"),
    path("delete_lesson/<int:lesson_id>", views.delete_lesson, name="delete_lesson"),
]