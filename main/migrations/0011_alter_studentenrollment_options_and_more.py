# Generated by Django 5.0.2 on 2024-03-13 18:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_studentenrollment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentenrollment',
            options={'verbose_name_plural': '6. Enrolled Courses'},
        ),
        migrations.AddField(
            model_name='studentenrollment',
            name='enrolled_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
