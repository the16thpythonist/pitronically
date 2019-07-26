# Django standard library imports
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from django.forms import FileInput

# Third party imports
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Project wide local imports
from .models import Project


User = get_user_model()


class ProjectAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        """
        The constructor.

        CHANGELOG

        Added 20.05.2019

        :param args:
        :param kwargs:
        """
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        # the 'fields' attribute is a list which contains the Field objects for the various fields.
        # the 'content' field is just TextField. Here we set the widget to be used to make an entry to this
        # textfield to the CKEditor visual post editor
        self.fields['content'].widget = CKEditorUploadingWidget()

    class Meta:
        fields = [
            "title",
            "subtitle",
            "slug",
            "content",
            "publishing_date",
            "creation_date",
            "next",
            "previous",
            "tags",
            "author",
            "thumbnail",
            "thumbnail_preview"
        ]
        model = Project


class ProjectAdmin(ModelAdmin):

    # 28.07.2019
    # Up to this point the list in the admin panel would just say "Project object(3)" for example and not have
    # any sort of information about what object was actually listed.
    list_display = ('title', 'author', 'creation_date')

    form = ProjectAdminForm


admin.site.register(Project, ProjectAdmin)
