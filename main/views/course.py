from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.models import Course
from main.paginators.course import CoursePaginator
from main.permissions.course import *
from main.seriallizers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == "create":
            permission_classes = [IsAuthenticated, IsNotModerator]
        elif self.action in ['update', 'partial_update, patch, put']:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action in ['retrieve']:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action in ['destroy']:
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]
