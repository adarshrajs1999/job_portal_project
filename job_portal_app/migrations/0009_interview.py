# Generated by Django 5.0.6 on 2024-06-22 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0008_remove_job_application_shortlist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('detail', models.TextField()),
                ('online_meet_link', models.TextField()),
                ('shortlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal_app.shortlist')),
            ],
        ),
    ]