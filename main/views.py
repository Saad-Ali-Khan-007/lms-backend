from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework import permissions
from .serializers import TeacherSerializer 
from rest_framework import generics
# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
