# Generated by Django 5.0.6 on 2024-06-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0010_rename_date_interview_interview_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='interview_task_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
