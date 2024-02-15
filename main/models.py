from django.db import models

# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 50)
    skills = models.TextField(max_length = 250)

    class Meta:
        verbose_name_plural = '1. Teachers'
    
    def __str__(self):
        return self.full_name

class CourseCategory(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)

    class Meta:
        verbose_name_plural = '2. Course Categories'
        
        
    def __str__(self):
        return self.title

class Course(models.Model):
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teachers_category = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    featured_img = models.ImageField(upload_to='course_imgs/',null=True)
    techs = models.TextField(null=True)

    class Meta:
        verbose_name_plural = '3. Courses'

    def __str__(self):
        return self.title
    
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='chapter_videos/',null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = '4. Chapter'
    

class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phone_no = models.IntegerField()
    qualification = models.CharField(max_length = 50)
    address = models.TextField(max_length = 250)
    interested_categories = models.TextField(max_length = 250)

    class Meta:
        verbose_name_plural = '5. Students'