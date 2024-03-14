from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework import permissions
from .serializers import TeacherSerializer 
from .serializers import CategorySerializer 
from .serializers import ViewCourseSerializer 
from .serializers import CourseSerializer 
from .serializers import ChapterSerializer 
from .serializers import UserSerializer 
from .serializers import StudentEnrollmentSerializer 
from rest_framework import generics
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        teacherData = models.Teacher.objects.get(email=email,password=password)
    except models.Teacher.DoesNotExist:
        teacherData =None
    if teacherData:
        return JsonResponse({"bool":True,'teacher_id':teacherData.id})  
    else:
        return JsonResponse({"bool":False})
    
class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer

class ViewCourseList(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = ViewCourseSerializer   

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset()
        if "result" in self.request.GET:
            limit = int(self.request.GET["result"])
            qs = models.Course.objects.all().order_by('-id')[:limit]

        if "category" in self.request.GET:
            category = self.request.GET['category']
            qs = models.Course.objects.filter(techs__icontains=category)

        if "skill_name" and "teacher_id" in self.request.GET:
            skill_name= self.request.GET['skill_name']
            teacher_id= self.request.GET['teacher_id']
            teacher = models.Teacher.objects.filter(id=teacher_id).first()
            qs = models.Course.objects.filter(techs__icontains=skill_name,teachers_category=teacher)
        return qs
    
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = ViewCourseSerializer
    
class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = ViewCourseSerializer
    
    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teachers_category=teacher)
    
class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    
   
    
class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class CourseChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer




class UserList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def user_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        userData = models.Student.objects.get(email=email,password=password)
    except models.Student.DoesNotExist:
        userData =None
    if userData:
        return JsonResponse({"bool":True,'user_id':userData.id})  
    else:
        return JsonResponse({"bool":False})
    
class StudentEnrollmentList(generics.ListCreateAPIView):
    queryset = models.StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer


def studentEnrollmentStatus(request,student_id,course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enrollStatus = models.StudentEnrollment.objects.filter(student=student,course=course)
    if enrollStatus:
        return JsonResponse({"bool":True})
    else:
        return JsonResponse({"bool":False})
    

class SpecificCourseEnrollrdStudent(generics.ListAPIView):
    queryset = models.StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.StudentEnrollment.objects.filter(course=course)