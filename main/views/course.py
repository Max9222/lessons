from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.models import Course
from main.seriallizers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = IsAuthenticated