# Generated by Django 2.1.8 on 2019-05-15 07:35

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image'),
        ),
    ]