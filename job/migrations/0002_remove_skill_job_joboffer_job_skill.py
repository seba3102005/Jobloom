# Generated by Django 5.2.1 on 2025-05-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='job',
        ),
        migrations.AddField(
            model_name='joboffer',
            name='job_skill',
            field=models.ManyToManyField(to='job.skill'),
        ),
    ]
