from django.db import models
from django.core import serializers

# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    profile_img = models.ImageField(upload_to="teacher_profile_imgs/", null=True)
    phone_no = models.CharField(max_length=11)
    qualification = models.CharField(max_length=50)
    skills = models.TextField(max_length=250)

    def skill_list(self):
        skill_list = self.skills.split(",")
        return skill_list

    def teacher_total_course_count(self):
        teacher_total_course_count = Course.objects.filter(
            teachers_category=self
        ).count()
        return teacher_total_course_count

    def teacher_all_students_count(self):
        teacher_all_students_count = StudentEnrollment.objects.filter(
            course__teachers_category=self
        ).count()
        return teacher_all_students_count

    def teacher_all_chapter_count(self):
        teacher_all_chapter_count = Chapter.objects.filter(
            course__teachers_category=self
        ).count()
        return teacher_all_chapter_count

    class Meta:
        verbose_name_plural = "1. Teachers"

    def __str__(self):
        return self.full_name


class CourseCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teachers_category = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="teacher_courses"
    )
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    featured_img = models.ImageField(upload_to="course_imgs/", null=True)
    techs = models.TextField(null=True)

    def related_courses(self):
        related_courses = Course.objects.filter(techs=self.techs).exclude(id=self.id)
        return serializers.serialize("json", related_courses)

    def tech_list(self):
        tech_list = self.techs.split(",")
        return tech_list

    def total_enrolled_students(self):
        total_enrolled_students = StudentEnrollment.objects.filter(course=self).count()
        return total_enrolled_students

    def average_course_rating(self):
        average_course_rating = Rating_Review.objects.filter(course=self).aggregate(
            avg_rating=models.Avg("rating")
        )
        return average_course_rating["avg_rating"]

    class Meta:
        verbose_name_plural = "3. Courses"

    def __str__(self):
        return self.title


class Chapter(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_chapters"
    )
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    video = models.FileField(upload_to="chapter_videos/", null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "4. Chapter"

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)
    profile_img = models.ImageField(upload_to="teacher_profile_imgs/", null=True)
    phone_no = models.CharField(max_length=11)
    qualification = models.CharField(max_length=50)
    address = models.TextField(max_length=250)
    interested_categories = models.TextField(max_length=250)

    def student_enrolled_course_count(self):
        student_enrolled_course_count = StudentEnrollment.objects.filter(
            student=self
        ).count()
        return student_enrolled_course_count

    def student_favourite_course_count(self):
        student_favourite_course_count = StudentFavouriteCourses.objects.filter(
            student=self
        ).count()
        return student_favourite_course_count

    def student_completed_assignment_count(self):
        student_completed_assignment_count = StudentAssignment.objects.filter(
            student=self, student_status=True
        ).count()
        return student_completed_assignment_count

    def student_pending_assignment_count(self):
        student_pending_assignment_count = StudentAssignment.objects.filter(
            student=self, student_status=False
        ).count()
        return student_pending_assignment_count

    class Meta:
        verbose_name_plural = "5. Students"

    def __str__(self):
        return self.full_name


class StudentEnrollment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrolled_course"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrolled_student"
    )
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "6. Enrolled Courses"

    def __str__(self):
        return f"{self.course}-{self.student}"


class Rating_Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "7. Enrolled Courses"

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"


class StudentFavouriteCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "8. Student Favourite Courses"


class StudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    student_status = models.BooleanField(default=False, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "9. Student Assignment"


class Notification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    notification_subject = models.CharField(max_length=200, null=True)
    notification_for = models.CharField(max_length=200)
    notification_created_time = models.DateTimeField(auto_now_add=True)
    notification_read_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "10. Notification"


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "11. Quiz"


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    right_ans = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "12. Quiz Questions"


class CourseQuiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "13. Course Quiz"
