from django.db import models
from django.core.validators import FileExtensionValidator
from course.models import Course

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(
        max_length=150,
        blank=False,
        default="New Lesson"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    slug = models.CharField(
        max_length=150,
        blank=False,
        default="" # Voeg als placeholder: `Descriptive short version of your title. SEO friendly`
    )

    content = models.TextField(
        max_length=2000,
        blank=True  # taal content van het les zoals `md` file
    )

    thumbnail = models.ImageField(
        upload_to="lesson_thumbnails/%y/%m/%d",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "png"]
            )
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Lesson"
        ordering = ["-created_at"]


