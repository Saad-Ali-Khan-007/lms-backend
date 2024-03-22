from django.contrib import admin
from . import models
from . import models

# Register your models here.
admin.site.register(models.Teacher)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.Student)
admin.site.register(models.StudentEnrollment)
admin.site.register(models.Rating_Review)
admin.site.register(models.StudentFavouriteCourses)
admin.site.register(models.StudentAssignment)


class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        "notification_subject",
        "notification_for",
        "notification_read_status",
    ]


admin.site.register(models.Notification, NotificationAdmin)

admin.site.register(models.Quiz)
admin.site.register(models.QuizQuestions)
admin.site.register(models.CourseQuiz)
admin.site.register(models.AttemptQuiz)
