from django.urls import path
from . import views

urlpatterns = [
    path("<slug:course_slug>", views.course_detail, name="course_detail"),
]