# Generated by Django 5.1.3 on 2024-12-02 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floodproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
    ]
