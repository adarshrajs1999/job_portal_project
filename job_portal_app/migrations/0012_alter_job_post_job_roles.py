# Generated by Django 5.0.6 on 2024-06-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0011_remove_job_post_job_role_job_post_job_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='job_roles',
            field=models.CharField(max_length=500),
        ),
    ]