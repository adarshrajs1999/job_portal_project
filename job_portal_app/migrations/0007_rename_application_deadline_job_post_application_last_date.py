# Generated by Django 5.0.6 on 2024-06-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0006_alter_jobseeker_profile_picture_job_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_post',
            old_name='application_deadline',
            new_name='application_last_date',
        ),
    ]