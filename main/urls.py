from rest_framework import routers

from main.apps import MainConfig

from django.urls import path


from main.views.lesson import *
from main.views.course import *
from main.views.payments import *

app_name = MainConfig.name

router = routers.SimpleRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('<int:pk>/delete/', LessonDestroyView.as_view(), name='lesson_delete'),

    path('payments/', PaymentsListView.as_view(), name='payments_list'),
    path('payments/create/', PaymentsCreateView.as_view(), name='payments_create'),
    path('payments/<int:pk>/', PaymentsRetrieveView.as_view(), name='payments_detail'),
    path('payments/<int:pk>/update/', PaymentsUpdateView.as_view(), name='payments_update'),
    path('payments/<int:pk>/delete/', PaymentsDestroyView.as_view(), name='payments_delete'),


] + router.urls
