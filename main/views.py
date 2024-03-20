from django.shortcuts import render
from . import models
from .serializers import TeacherSerializer
from .serializers import CategorySerializer
from .serializers import ViewCourseSerializer
from .serializers import CourseSerializer
from .serializers import ChapterSerializer
from .serializers import UserSerializer
from .serializers import StudentEnrollmentSerializer
from .serializers import ViewStudentEnrollmentSerializer
from .serializers import CourseRatingAndReviewSerializer
from .serializers import TeacherDashboardSerializer
from .serializers import StudentFavouriteCoursesSerializer
from .serializers import StudentAssignmentSerializer
from .serializers import UserDashboardSerializer
from .serializers import NotificationSerializer
from .serializers import QuizSerializer
from .serializers import QuizQuestionSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDashboard(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherDashboardSerializer


@csrf_exempt
def teacher_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        teacherData = models.Teacher.objects.get(email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        return JsonResponse({"bool": True, "teacher_id": teacherData.id})
    else:
        return JsonResponse({"bool": False})


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer


class ViewCourseList(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = ViewCourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if "result" in self.request.GET:
            limit = int(self.request.GET["result"])
            qs = models.Course.objects.all().order_by("-id")[:limit]

        if "category" in self.request.GET:
            category = self.request.GET["category"]
            qs = models.Course.objects.filter(techs__icontains=category)

        if "skill_name" and "teacher_id" in self.request.GET:
            skill_name = self.request.GET["skill_name"]
            teacher_id = self.request.GET["teacher_id"]
            teacher = models.Teacher.objects.filter(id=teacher_id).first()
            qs = models.Course.objects.filter(
                techs__icontains=skill_name, teachers_category=teacher
            )

        elif "student_id" in self.kwargs:
            student_id = self.kwargs["student_id"]
            student = models.Student.objects.get(pk=student_id)

            queries = [
                Q(techs__iendswith=value) for value in student.interested_categories
            ]

            query = queries.pop()
            for item in queries:

                query |= item
            qs = models.Course.objects.filter(query)

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
        teacher_id = self.kwargs["teacher_id"]
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
        course_id = self.kwargs["course_id"]
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class UserList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = UserSerializer


class UserDashboard(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = UserDashboardSerializer


@csrf_exempt
def user_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        userData = models.Student.objects.get(email=email, password=password)
    except models.Student.DoesNotExist:
        userData = None
    if userData:
        return JsonResponse({"bool": True, "user_id": userData.id})
    else:
        return JsonResponse({"bool": False})


@csrf_exempt
def user_forgot_password(request, student_id):
    password = request.POST["password"]
    try:
        studentData = models.Student.objects.get(id=student_id)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        models.Student.objects.filter(id=student_id).update(password=password)
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


class StudentEnrollmentList(generics.ListCreateAPIView):
    queryset = models.StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer


class ViewStudentEnrollmentList(generics.ListAPIView):
    queryset = models.StudentEnrollment.objects.all()
    serializer_class = ViewStudentEnrollmentSerializer


def studentEnrollmentStatus(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enrollStatus = models.StudentEnrollment.objects.filter(
        student=student, course=course
    )
    if enrollStatus:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


class SpecificCourseEnrolledStudent(generics.ListAPIView):
    queryset = models.StudentEnrollment.objects.all()
    serializer_class = ViewStudentEnrollmentSerializer

    def get_queryset(self):
        if "course_id" in self.kwargs:
            course_id = self.kwargs["course_id"]
            course = models.Course.objects.get(pk=course_id)
            return models.StudentEnrollment.objects.filter(course=course)
        elif "teacher_id" in self.kwargs:
            teacher_id = self.kwargs["teacher_id"]
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentEnrollment.objects.filter(
                course__teachers_category=teacher
            ).distinct()
        elif "student_id" in self.kwargs:
            student_id = self.kwargs["student_id"]
            student = models.Student.objects.get(pk=student_id)
            return models.StudentEnrollment.objects.filter(student=student).distinct()


class CourseRatingAndReview(generics.ListCreateAPIView):
    serializer_class = CourseRatingAndReviewSerializer

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        course = models.Course.objects.get(pk=course_id)
        return models.Rating_Review.objects.filter(course=course)


def studentRatingStatus(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    ratingStatus = models.Rating_Review.objects.filter(student=student, course=course)
    if ratingStatus:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


@csrf_exempt
def teacher_forgot_password(request, teacher_id):
    password = request.POST["password"]
    try:
        teacherData = models.Teacher.objects.get(id=teacher_id)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        models.Teacher.objects.filter(id=teacher_id).update(password=password)
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


class StudentFavouriteCourse(generics.ListCreateAPIView):
    queryset = models.StudentFavouriteCourses.objects.all()
    serializer_class = StudentFavouriteCoursesSerializer

    def get_queryset(self):

        if "student_id" in self.kwargs:
            student_id = self.kwargs["student_id"]
            student = models.Student.objects.get(pk=student_id)
            return models.StudentFavouriteCourses.objects.filter(
                student=student
            ).distinct()


def favourite_status(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    favourite_status = models.StudentFavouriteCourses.objects.filter(
        course=course, student=student
    ).first()
    if favourite_status:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


def remove_favourite(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    remove_favourite = models.StudentFavouriteCourses.objects.filter(
        course=course, student=student
    ).delete()
    if remove_favourite:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


class StudentAssignment(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        teacher_id = self.kwargs["teacher_id"]
        student = models.Student.objects.get(pk=student_id)
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.StudentAssignment.objects.filter(student=student, teacher=teacher)


class TeacherAssignment(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        student_id = self.kwargs["student_id"]

        student = models.Student.objects.get(pk=student_id)

        models.Notification.objects.filter(
            student=student,
            notification_subject="assignment",
            notification_for="student",
        ).update(
            notification_read_status=True,
        )

        return models.StudentAssignment.objects.filter(student=student)


class StudentAssignmentStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer


class NotificationList(generics.ListCreateAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        student = models.Student.objects.get(pk=student_id)
        return models.Notification.objects.filter(
            student=student,
            notification_subject="assignment",
            notification_for="student",
            notification_read_status=False,
        )


class QuizList(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        teacher_id = self.kwargs["teacher_id"]
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Quiz.objects.filter(teacher=teacher)


class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizQuestionList(generics.ListCreateAPIView):
    queryset = models.QuizQuestions.objects.all()
    serializer_class = QuizQuestionSerializer


class CourseQuizQuestionList(generics.ListAPIView):
    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs["quiz_id"]
        quiz = models.Quiz.objects.get(pk=quiz_id)
        return models.QuizQuestions.objects.filter(quiz=quiz)


class CourseQuizQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuizQuestions.objects.all()
    serializer_class = QuizQuestionSerializer
