# Generated by Django 5.0 on 2023-12-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
