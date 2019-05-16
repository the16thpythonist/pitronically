# Generated by Django 2.1.8 on 2019-05-15 14:14

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0007_auto_20190515_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tags',
        ),
        migrations.AddField(
            model_name='project',
            name='tagss',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tagss',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
