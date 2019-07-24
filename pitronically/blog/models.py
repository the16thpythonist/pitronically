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
        """
        Returns a list with the n most recent projects

        CHANGELOG

        Added 20.05.2019

        Changed 24.07.2019
        Changed it so that the ordering is now descending

        :param n:
        :return:
        """
        # 24.07.2019
        # In Django models the "order_by" by method takes the name of the class variable, which contains the field to
        # order by. If a reverse order by this field is desired, one just needs to add a minus in front of the name:
        projects = cls.objects.order_by("-publishing_date").exclude(publishing_date__gte=timezone.now()).all()[0:n]
        return list(projects)


class Project(Entry):
    author = ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="projects")
    thumbnail = FilerImageField(related_name="project_thumbnail", on_delete=models.CASCADE)
    thumbnail_preview = FilerImageField(related_name="project_thumbnail_preview", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog:project_detail", kwargs={"pk": self.id})


class Tutorial(Entry):
    author = ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="tutorials")
    pass



