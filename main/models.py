from django.db import models
from django.core import serializers
# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length = 50)
    description = models.TextField(null=True)
    email = models.CharField(max_length = 50,unique=True)
    password = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 11)
    qualification = models.CharField(max_length = 50)
    skills = models.TextField(max_length = 250)

    def skill_list(self):
        skill_list = self.skills.split(',')
        return skill_list

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
    teachers_category = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teacher_courses")
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    featured_img = models.ImageField(upload_to='course_imgs/',null=True)
    techs = models.TextField(null=True)


    def related_courses(self):
        related_courses = Course.objects.filter(techs=self.techs)
        return serializers.serialize('json',related_courses)
    
    def tech_list(self):
        tech_list = self.techs.split(',')
        return tech_list
    
    class Meta:
        verbose_name_plural = '3. Courses'

    def __str__(self):
        return self.title
    
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_chapters")
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='chapter_videos/',null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = '4. Chapter'
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length=11)
    qualification = models.CharField(max_length = 50)
    address = models.TextField(max_length = 250)
    interested_categories = models.TextField(max_length = 250)

    class Meta:
        verbose_name_plural = '5. Students'

    def __str__(self):
        return self.full_name

class StudentEnrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="enrolled_course")
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="enrolled_student")
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '6. Enrolled Courses'
   

    def __str__(self):
       return f"{self.course}-{self.student}"
   