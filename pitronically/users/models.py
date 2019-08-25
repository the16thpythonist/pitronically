import tempfile
import urllib3
import os

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, TextField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import django.db.models as models

from django.core.files import File
from django.conf import settings

# Third party imports
from filer.fields.image import FilerImageField
from imagekit import ImageSpec
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class ProfileImage(ImageSpec):
    """
    Extends "ImageSpec".
    ImageSpec is a class from the django-imagekit package, which is used to make various transformations of images.
    The ProfileImage class implements a special transformation: The image will be resized to a 50x50 px image and
    saved in the JPEG format.

    CHANGELOG

    Added 18.06.2019
    """
    processors = [ResizeToFill(50, 50)]
    format = 'JPEG'
    options = {'quality': 60}


class User(AbstractUser):
    """
    CHANGELOG

    Added 20.05.2019
    """
    profile_icon_created = False

    # It is important, that all fields additionally defined for the user model are NOT mandatory, because during the
    # very first "createsuperuser" process of Django a custom mandatory field could not be filled in resulting in an
    # error.

    # First Name and Last Name do not cover name patterns
    # around the globe, thus we use one field, where the full name should be inserted
    name = CharField(_("Name of User"), blank=True, max_length=255)

    # A FilerImageField is a field, which will automatically expose a Filer file upload widget to the admin backend,
    # through which an image file can either be selected from the already existent filer storage folders or freshly
    # be uploaded
    image = FilerImageField(null=True, blank=True, related_name="user_profile_image", on_delete=models.CASCADE)

    # This field will contain the small 50x50px version of the profile image. It will not be directly uploaded by
    # the user, but rather automatically be created from the full size version of the image during the save process
    # of the model.
    profile_icon = ImageField(null=True, blank=True)

    # 21.07.2019
    # This field should contain a short introductory text about the people, like "Hi I am mike from oregon and I just
    # wanna write some stupid shit on this site my interests are.."
    introduction = TextField(_("Introduce yourself"), blank=True)
    # This will contain the age of the member
    age = IntegerField(_("Your Age"), null=True, blank=True)
    country = CharField(_("Your Country"), blank=True, max_length=255)
    profession = CharField(_("Current profession"), blank=True, max_length=255)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def get_recent_projects(self, n=5):
        """
        Returns the n latest project posts for this user

        CHANGELOG

        Added 21.07.2019

        :param n:
        :return:
        """
        recent_projects = self.projects.order_by('publishing_date')[0:5]
        return recent_projects

    def get_absolute_url(self):
        """
        Returns the full URL to the web page of this user

        CHANGELOG

        Added 20.05.2019

        :return:
        """
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        """
        This method is being called, when the model is being saved.
        Here we implement the custom behaviour, which creates the 150x50 profile icon from the uploaded full size
        image.

        CHANGELOG

        Added 18.07.2019

        :param args:
        :param kwargs:
        :return:
        """
        # It is important, that the creation of the profile icon is executed after the super() save process, because
        # the base image for the transform within "self.image" might not already be saved as file.
        super(User, self).save(*args, **kwargs)

        if self.image and not self.profile_icon_created:
            # This method will create a 50x50 px version of the Image uploaded to "self.image" and save it to the
            # "self.profile_icon" field. At the end it sets self.profile_icon_created to True to prevent a
            # recursion during the save process.
            self._create_profile_icon()

    def _create_profile_icon(self):
        """
        This method creates the profile icon image, which is a 50x50 px Version of the profile picture, which was
        uploaded by the user and saves it to the "profile_icon" ImageField of the User model.

        CHANGELOG

        Added 18.07.2019

        :return:
        """
        # !! Since the media will be going to the amazon bucket i might have to change this to first download the file
        # via urllib first

        # "self.image" is of the type "Image" from the Filer package.
        # The "file_ptr" attribute is a one to one field mapping to a Filer "File" model, which saves the location
        # of the file. The "path" property of this "File" object now finally contains the full path of the file
        # on the system
        image_bytes = self._get_profile_image_content()
        source_file = tempfile.TemporaryFile()
        source_file.write(image_bytes)

        image_generator = ProfileImage(source=source_file)

        # The "generate" method returns a "_io.BytesIO" object, which describes the byte string for the resulting
        # image file. But we need the actual byte string. It can be extracted from the BytesIO object using its
        # "getvalue" method which returns a normal python byte string
        result_bytesio = image_generator.generate()
        result_bytes = result_bytesio.getvalue()

        # Here we create a temporary file. We simply need it because it works the same way as a normal python file
        # descriptor. A file descriptor is needed to save the "ImageField"
        result_file = tempfile.TemporaryFile()
        result_file.write(result_bytes)

        # "profile_icon_created" is a class attribute, which is initially False. The creation of the profile image
        # will only be triggered if it is False. We need to set it to True, because the "save" method on the
        # profile_icon "ImageField" triggers a save for the whole User for some reason, which would create an
        # infinite recursion.
        self.profile_icon_created = True
        self.profile_icon.save(
            self.name + '_profile.jpeg',
            File(result_file)
        )

        source_file.close()

    def _get_profile_image_content(self):
        """
        Returns a byte string, which resembles the content of the image file, which was uploaded as the profile
        picture of the user.

        CHANGELOG

        Added 20.07.2019

        :return:
        """
        if settings.IS_PRODUCTION:
            return self._get_profile_image_content_by_url()
        else:
            return self._get_profile_image_content_by_path()

    def _get_profile_image_content_by_path(self):
        """
        Returns a byte string, which resembled the content of the image file, which was uploaded as the profile
        picture of the user. It does so by getting the actual physical path of the image file from the hard drive
        and reading this files content.

        CHANGELOG

        Added 20.07.2019

        :return:
        """
        # "self.image" is of the type "Image" from the Filer package.
        # The "file_ptr" attribute is a one to one field mapping to a Filer "File" model, which saves the location
        # of the file. The "path" property of this "File" object now finally contains the full path of the file
        # on the system
        path = self.image.file_ptr.path
        with open(path, mode='rb') as image:
            return image.read()

    def _get_profile_image_content_by_url(self):
        """
        Returns a byte string, which resembles the content of the image file, which was uploaded as the profile
        picture of the user. It does so by downloading the content from the url of the image file within the media
        folder of the website.

        CHANGELOG

        Added 20.07.2019

        :return:
        """
        # "self.image" is of the type "Image" from the Filer package.
        # The "file_ptr" attribute is a one to one field mapping to a Filer "File" model, which saves the location
        # of the file. The "path" property of this "File" object now finally contains the full path of the file
        # on the system
        url = self.image.file_ptr.url
        http = urllib3.PoolManager()
        with http.request('GET', url, preload_content=False) as image:
            return image.read()
