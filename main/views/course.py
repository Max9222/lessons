from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.models import Course
from main.paginators.course import CoursePaginator
from main.permissions.course import *
from main.seriallizers.course import CourseSerializer
from main.tasks import send_massage_add_materials


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

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.owner = self.request.user
        new_lesson.save()
        if new_lesson:
            send_massage_add_materials.delay(new_lesson.course.id)
