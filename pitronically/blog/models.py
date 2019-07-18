# Python standard library imports
import datetime

# Django core library imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model
from django.db.models import SlugField, CharField, TextField, DateTimeField, URLField, ManyToManyField, ForeignKey, ImageField
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.forms import FileInput

# Third party imports
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from filer.fields.image import FilerImageField
from taggit.managers import TaggableManager

# Project local imports
from pitronically.users.models import User


class Entry(models.Model):
    author = ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = CharField(max_length=250)
    slug = SlugField(max_length=100, default='slug')
    subtitle = CharField(max_length=250, default="")
    content = TextField(default="")
    publishing_date = DateTimeField(default=timezone.now)
    creation_date = DateTimeField(default=timezone.now)
    next = URLField(null=True, blank=True)
    previous = URLField(null=True, blank=True)
    tags = TaggableManager()

    class Meta:
        abstract = True

    @classmethod
    def most_recent(cls, n: int):
        projects = cls.objects.order_by("publishing_date").exclude(publishing_date__gte=timezone.now()).all()[0:n]
        return list(projects)


class Project(Entry):
    thumbnail = FilerImageField(related_name="project_thumbnail", on_delete=models.CASCADE)
    thumbnail_preview = FilerImageField(related_name="project_thumbnail_preview", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog:project_detail", kwargs={"pk": self.id})


class Tutorial(Entry):
    pass



