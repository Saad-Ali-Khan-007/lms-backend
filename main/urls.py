from django.urls import path
from . import views
urlpatterns = [
    # teacher
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('teachers/login/',views.teacher_login),
    
    # category
    path('category/',views.CategoryList.as_view()),
    
    # course
    path('course/',views.CourseList.as_view()),

    path('course/<int:pk>',views.CourseDetail.as_view()),

    # chapter
    path('chapter/',views.ChapterList.as_view()),

    path('chapter/<int:pk>',views.ChapterDetail.as_view()),

    # chapter a/c to courses
    path('course-chapters/<int:course_id>',views.CourseChapterList.as_view()),
    
    # teacher course list
    
    path('teacher-courses/<int:teacher_id>/',views.TeacherCourseList.as_view()),

    path('teacher-course-detail/<int:pk>',views.TeacherCourseDetail.as_view())
]