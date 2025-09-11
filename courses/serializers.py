from rest_framework import serializers
from .models import Course, Module, Lesson, Enrollment
from django.contrib.auth.models import User

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "order"]

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ["id", "title", "order", "lessons"]

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    instructor = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'  # Use username to match "Theoneste"
    )
   

    class Meta:
        model = Course
        fields = ["id", "title", "description","instructor", "created_at", "updated_at", "modules"]
  

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = ["id", "student", "course", "enrolled_at"]
        read_only_fields = ["student", "enrolled_at"]