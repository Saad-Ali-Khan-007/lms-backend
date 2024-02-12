from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework import permissions
from .serializers import TeacherSerializer 
from rest_framework import generics
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

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
    teacherData = models.Teacher.objects.get(email=email,password=password)
    if teacherData:
        return JsonResponse({"bool":True})  
    else:
        return JsonResponse({"bool":False})