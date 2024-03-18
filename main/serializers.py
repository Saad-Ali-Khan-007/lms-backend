from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
            "id",
            "full_name",
            "description",
            "email",
            "password",
            "profile_img",
            "phone_no",
            "qualification",
            "skills",
            "teacher_courses",
            "skill_list",
        ]
        depth = 1


class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
            "full_name",
            "qualification",
            "profile_img",
            "teacher_total_course_count",
            "teacher_all_students_count",
            "teacher_all_chapter_count",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = "__all__"


class ViewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            "id",
            "course_category",
            "teachers_category",
            "title",
            "description",
            "featured_img",
            "techs",
            "course_chapters",
            "related_courses",
            "tech_list",
            "total_enrolled_students",
            "average_course_rating",
        ]
        depth = 1


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            "id",
            "course_category",
            "teachers_category",
            "title",
            "description",
            "featured_img",
            "techs",
        ]


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentEnrollment
        fields = "__all__"


class ViewStudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentEnrollment
        fields = ["id", "course", "student", "enrolled_time"]
        depth = 2


class CourseRatingAndReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating_Review
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CourseRatingAndReviewSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1


class StudentFavouriteCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentFavouriteCourses
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentFavouriteCoursesSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 2


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1
