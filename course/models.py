from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from account.models import Profile

class Course(models.Model):
    name = models.CharField(
        max_length=50,
        default="category name",
        verbose_name="name",
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        max_length=60,
        unique=True,
        blank=True,
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
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

