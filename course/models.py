from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

class Course(models.Model):
    name = models.CharField(
        max_length=50,
        default="category name",
        verbose_name="name",
        blank=False,
        null=False,
    )
    description = models.TextField(
        max_length=2000,
        blank=True
    )

    auther = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True
    )


    icon = models.ImageField(
        "Icon",
        upload_to="",
        blank=False,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "png",
                    "jpg",
                    "gif"
                ]
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
        return self.name

