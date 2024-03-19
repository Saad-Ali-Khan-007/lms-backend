from django.urls import path
from . import views

urlpatterns = [
    # teacher
    path("teachers/", views.TeacherList.as_view()),
    path("teachers/<int:pk>/", views.TeacherDetail.as_view()),
    path("teacher-forgot-password/<int:teacher_id>/", views.teacher_forgot_password),
    path("teacher-dashboard/<int:pk>/", views.TeacherDashboard.as_view()),
    path("teachers/login/", views.teacher_login),
    # category
    path("category/", views.CategoryList.as_view()),
    # course
    path("add-course/", views.CourseList.as_view()),
    path("course/", views.ViewCourseList.as_view()),
    path("course/<int:pk>", views.CourseDetail.as_view()),
    # chapter
    path("chapter/", views.ChapterList.as_view()),
    path("chapter/<int:pk>", views.ChapterDetail.as_view()),
    # chapter a/c to courses
    path("course-chapters/<int:course_id>", views.CourseChapterList.as_view()),
    # teacher course list
    path("teacher-courses/<int:teacher_id>/", views.TeacherCourseList.as_view()),
    path("teacher-course-detail/<int:pk>", views.TeacherCourseDetail.as_view()),
    # Student
    path("users/", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
    path("user/login/", views.user_login),
    path("user-forgot-password/<int:student_id>/", views.user_forgot_password),
    # Student enroll in course
    path("enroll-course/", views.StudentEnrollmentList.as_view()),
    path("enrolled-course/", views.ViewStudentEnrollmentList.as_view()),
    # Student enroll Status
    path(
        "enroll-status/<int:student_id>/<int:course_id>/", views.studentEnrollmentStatus
    ),
    # Students enrolled in specfic course
    path(
        "student-enrolled-course/<int:course_id>/",
        views.SpecificCourseEnrolledStudent.as_view(),
    ),
    path(
        "teacher-all-student/<int:teacher_id>/",
        views.SpecificCourseEnrolledStudent.as_view(),
    ),
    path(
        "student-dashboard/<int:pk>/",
        views.UserDashboard.as_view(),
    ),
    path(
        "student-course/<int:student_id>/",
        views.SpecificCourseEnrolledStudent.as_view(),
    ),
    path(
        "student-recommended-course/<int:student_id>/",
        views.ViewCourseList.as_view(),
    ),
    path(
        "student-favourite-course/",
        views.StudentFavouriteCourse.as_view(),
    ),
    path(
        "specific-student-favourite-course/<int:student_id>/",
        views.StudentFavouriteCourse.as_view(),
    ),
    path(
        "student-favourite-course-status/<int:student_id>/<int:course_id>/",
        views.favourite_status,
    ),
    path(
        "student-remove-favourite-course/<int:student_id>/<int:course_id>/",
        views.remove_favourite,
    ),
    path(
        "student-remove-favourite-course/<int:student_id>/<int:course_id>/",
        views.remove_favourite,
    ),
    # course rating and review
    path("course-rating-review/<int:course_id>", views.CourseRatingAndReview.as_view()),
    path("rating-status/<int:student_id>/<int:course_id>/", views.studentRatingStatus),
    path(
        "student-assignment/<int:student_id>/<int:teacher_id>/",
        views.StudentAssignment.as_view(),
    ),
    path(
        "teacher-assigned-assignment/<int:student_id>/",
        views.TeacherAssignment.as_view(),
    ),
    path(
        "student-mark-assignment/<int:pk>/",
        views.StudentAssignmentStatus.as_view(),
    ),
]
