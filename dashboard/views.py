from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from course.models import Course
from lesson.models import Lesson
from account.forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from account.models import Profile
from lesson.forms import CourseForm
from course.forms import LessonForm


def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/dashboard.html", context={

        })
    
    messages.error("Please login or create an account first.")
    return redirect("login")

@login_required
def profile_view(request):
    """
    Toont en verwerkt het gebruikersprofiel.
    Werkt met een bestaand Profile-object (UPDATE, geen CREATE).
    """

    # Zorg dat het profiel bestaat
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    print(profile)

    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")  # naam van je url

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "active_tab": "profile",
        "image_file": (
            profile.picture.url
            if profile.picture
            else None
        ),
    }

    return render(
        request,
        "dashboard/profile.html",
        context
    )


def new_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.cleaned_data["course"]
            if course.auther != request.user:
                messages.error(request, "You are not the author of the selected course.")
                return redirect('new_lesson')
            form.save()
            return redirect('dashboard')  # of naar dezelfde pagina
    else:
        form = LessonForm(user= request.user)
    return render(request, 'dashboard/new_lesson.html', {'new_lesson_form': form, 'new_course_form': CourseForm(), "active_tab": "new_lesson",})



def new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.auther = request.user
            course.save()
            return redirect('new_lesson')
    else:
        form = CourseForm()
    return render(request, 'dashboard/new_lesson.html', {'new_lesson_form': LessonForm(), 'new_course_form': form, "active_tab": "new_lesson",})


def user_lessons(request):
    current_user_lessons = Lesson.objects.filter(
        course__auther=request.user
    )
    context = {
        "current_user_lessons": current_user_lessons,
        "active_tab": "user_lessons",
    }
    return render(request, 'dashboard/user_lessons.html', context)



def update_lesson(request, lesson_id):

    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect("user_lessons")
    else:
        form = LessonForm(instance=lesson)

    context = {
        "form": form,
        "lesson": lesson,
        "active_tab": "user_lessons",
    }
    return render(request, "dashboard/update_lesson.html", context)



def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if lesson:
        lesson.delete()
        messages.info(message="Lesson is deleted!")
        return redirect("user_lessons")
    messages.error(message="Could not deleting the lesson!")
    return redirect("user_lessons")



