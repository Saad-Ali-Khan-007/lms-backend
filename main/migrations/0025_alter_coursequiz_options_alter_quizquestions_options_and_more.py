# Generated by Django 5.0.2 on 2024-03-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_quiz_coursequiz_quizquestions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursequiz',
            options={'verbose_name_plural': '13. Course Quiz'},
        ),
        migrations.AlterModelOptions(
            name='quizquestions',
            options={'verbose_name_plural': '12. Quiz Questions'},
        ),
        migrations.AddField(
            model_name='coursequiz',
            name='assign_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
