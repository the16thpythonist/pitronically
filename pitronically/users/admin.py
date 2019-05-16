import os

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# Third party imports
from filebrowser.fields import FileBrowseWidget
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill


class ProfileImage(ImageSpec):
    processors = [ResizeToFill(50, 50)]
    format = 'JPEG'
    options = {'quality': 60}

# Project local imports
from pitronically.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()






@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name", "image",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(auth_admin.UserAdmin, self).__init__(*args, **kwargs)

    def save_model(self, request, obj, form, change):

        if obj.image:
            source_path = obj.image.path_full
            source_file = open(source_path, "rb")
            image_generator = ProfileImage(source=source_file)
            result = image_generator.generate()
            obj.profile_image.save(
                os.path.basename(source_path).split('.')[0] + "_profile.jpeg",
                result
            )

        super(UserAdmin, self).save_model(request, obj, form, change)

