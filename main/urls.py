from django.urls import path
from . import views
urlpatterns = [
    # teacher
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-forgot-password/<int:teacher_id>/', views.teacher_forgot_password),
    path('teachers/login/',views.teacher_login),
    
    # category
    path('category/',views.CategoryList.as_view()),
    
    # course
    path('add-course/',views.CourseList.as_view()),

    path('course/',views.ViewCourseList.as_view()),


    path('course/<int:pk>',views.CourseDetail.as_view()),

    # chapter
    path('chapter/',views.ChapterList.as_view()),

    path('chapter/<int:pk>',views.ChapterDetail.as_view()),

    # chapter a/c to courses
    path('course-chapters/<int:course_id>',views.CourseChapterList.as_view()),
    
    # teacher course list
    
    path('teacher-courses/<int:teacher_id>/',views.TeacherCourseList.as_view()),

    path('teacher-course-detail/<int:pk>',views.TeacherCourseDetail.as_view()),


    # Student

    path('users/',views.UserList.as_view()),

    path('user/login/',views.user_login),


    # Student enroll in course


    path('enroll-course/',views.StudentEnrollmentList.as_view()),

    path('enrolled-course/',views.ViewStudentEnrollmentList.as_view()),
    # Student enroll Status

    path('enroll-status/<int:student_id>/<int:course_id>/',views.studentEnrollmentStatus),


    # Students enrolled in specfic course

    path('student-enrolled-course/<int:course_id>/',views.SpecificCourseEnrolledStudent.as_view()),



    path('teacher-all-student/<int:teacher_id>/',views.SpecificCourseEnrolledStudent.as_view()),


    # course rating and review

    path('course-rating-review/<int:course_id>',views.CourseRatingAndReview.as_view()),


    path('rating-status/<int:student_id>/<int:course_id>/',views.studentRatingStatus),


]