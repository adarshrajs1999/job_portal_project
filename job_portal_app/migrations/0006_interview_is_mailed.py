# Generated by Django 5.0.6 on 2024-06-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0005_rename_mail_hire_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='is_mailed',
            field=models.BooleanField(default=0),
        ),
    ]
