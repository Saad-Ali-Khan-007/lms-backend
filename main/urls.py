from django.urls import path
from . import views
urlpatterns = [
    # teacher
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('teachers/login/',views.teacher_login),
    
    # category
    path('category/',views.CategoryList.as_view()),
]