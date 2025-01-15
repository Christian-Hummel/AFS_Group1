# Generated by Django 5.1.3 on 2025-01-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodproject', '0024_alter_customuser_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='customuser',
            name='latitude',
            field=models.FloatField(default=47.4231277, max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='longitude',
            field=models.FloatField(default=13.6539813, max_length=10),
        ),
    ]
