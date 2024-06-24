# Generated by Django 5.0.6 on 2024-06-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0006_interview_is_mailed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hire',
            old_name='contact_info',
            new_name='address_and_contact',
        ),
        migrations.AlterField(
            model_name='hire',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]