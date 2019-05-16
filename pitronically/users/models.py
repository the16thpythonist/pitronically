from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Third party imports
from filebrowser.fields import FileBrowseField
from filebrowser.base import FileObject
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    image = FileBrowseField("Image",
                            max_length=200,
                            directory="uploads",
                            extensions=[".png", ".jpg", ".jpeg"],
                            null=True,
                            blank=True)
    profile_image = ImageField(blank=True, upload_to="uploads")

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


