# Generated by Django 5.0.2 on 2024-03-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rating_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='teacher_profile_imgs/'),
        ),
    ]
