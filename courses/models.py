from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Course title")
    description = models.TextField(verbose_name="Course description", blank=True)
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_taught"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=200, verbose_name="Module title")
    description = models.TextField(verbose_name="Module description", blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"
        ordering = ["order"]
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name="lessons"
    )
    title = models.CharField(max_length=200, verbose_name="Lesson title")
    content = models.TextField(verbose_name="Lesson description", blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["order"]
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="enrolled_courses"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolled_students")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ["student", "course"]
        
    def __str__(self):
        return f"{self.student.username} - {self.course.title}"