# Generated by Django 5.1.3 on 2024-12-10 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodproject', '0009_customuser_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='upvote',
        ),
        migrations.AddField(
            model_name='vote',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='vote',
            name='validity',
            field=models.BooleanField(default=True),
        ),
    ]
