# Generated by Django 5.0.6 on 2024-06-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_application',
            name='shortlist_status',
            field=models.BooleanField(default=0),
        ),
    ]