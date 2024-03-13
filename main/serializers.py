from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ["id","full_name","description","email","password","phone_no","qualification","skills","teacher_courses","skill_list"]
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = '__all__'
        
        
class ViewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ["id","course_category","teachers_category","title","description","featured_img","techs","course_chapters","related_courses","tech_list"]
        depth = 1

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ["id","course_category","teachers_category","title","description","featured_img","techs"]
   


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = '__all__'