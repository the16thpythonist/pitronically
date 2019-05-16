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
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = CKEditorUploadingWidget()

    class Meta:
        fields = ["title", "subtitle", "slug", "content", "publishing_date", "creation_date", "next", "previous", "tagss", "author", "thumbnail", "thumbnail_preview"]
        model = Project


class ProjectAdmin(ModelAdmin):
    form = ProjectAdminForm


admin.site.register(Project, ProjectAdmin)
