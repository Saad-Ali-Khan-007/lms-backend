# Generated by Django 5.0.2 on 2024-03-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_teacher_description_alter_chapter_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
    ]
