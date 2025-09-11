from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Course, Enrollment, Lesson, Module
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer, EnrollmentSerializer
from .permissions import IsInstructorsOnly, IsOwnEnrollment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsInstructorsOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['instructor']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'description']

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all() 
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsInstructorsOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'description']

# Lesson view sets
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsInstructorsOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['module']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'description']

# Enrollment view sets
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsOwnEnrollment]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['student', 'course']
    search_fields = ['student__username', 'course__title']
    ordering_fields = ['enrolled_at']
    