# Generated by Django 5.0.6 on 2024-06-15 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0013_rename_qualification_job_post_educational_qualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_post',
            old_name='image',
            new_name='poster_image',
        ),
    ]
