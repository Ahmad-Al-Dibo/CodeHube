from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator, EmailValidator
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(
        unique=True, 
        validators=[
            EmailValidator()
        ]
    )
    first_name = models.CharField(
        max_length=150, 
        blank=False, 
        null=False, 
        default=""
    )
    last_name = models.CharField(
        max_length=150, 
        blank=False, 
        null=False, 
        default=""
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "User"
        ordering = ["first_name"]



class Profile(models.Model):
    """
    Profielmodel voor aanvullende gebruikersinformatie.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    bio = models.TextField(
        max_length=2000,
        blank=True
    )

    picture = models.ImageField(
        upload_to="photos/%y/%m/%d",
        verbose_name="Photo",
        default="photos/default/default.png",
        blank=True,
        null=False
    )

    cv = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx"]
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
        return f"Profile({self.user.email})"


class Sessions(models.Model):
    """
    Model voor het bijhouden van gebruikerssessies.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sessions"
    )

    session_token = models.CharField(
        max_length=255,
        unique=True
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
        return f"Session({self.user.email}, {self.session_token})"