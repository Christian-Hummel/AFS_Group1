# Generated by Django 5.1.3 on 2025-01-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodproject', '0027_rename_assigneddate_task_assigned_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='latitude',
            field=models.FloatField(default=47.4231277, max_length=10),
        ),
        migrations.AddField(
            model_name='task',
            name='longitude',
            field=models.FloatField(default=13.6539813, max_length=10),
        ),
    ]
