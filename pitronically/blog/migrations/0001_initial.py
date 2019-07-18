# Generated by Django 2.1.8 on 2019-05-18 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='slug', max_length=100)),
                ('subtitle', models.CharField(default='', max_length=250)),
                ('content', models.TextField(default='')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('next', models.URLField(blank=True, null=True)),
                ('previous', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('thumbnail', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='project_thumbnail', to=settings.FILER_IMAGE_MODEL)),
                ('thumbnail_preview', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='project_thumbnail_preview', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='slug', max_length=100)),
                ('subtitle', models.CharField(default='', max_length=250)),
                ('content', models.TextField(default='')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('next', models.URLField(blank=True, null=True)),
                ('previous', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
