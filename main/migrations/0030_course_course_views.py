# Generated by Django 5.0.2 on 2024-03-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_studymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_views',
            field=models.BigIntegerField(default=0),
        ),
    ]
