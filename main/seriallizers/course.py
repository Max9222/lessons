from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from main.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    # last_amount = serializers.IntegerField(source='amount_set.all.first.amount')
    lesson = SlugRelatedField(slug_field='name', queryset=Lesson.objects.all())  # Название урока вместо цифры
    count = SerializerMethodField()

    def get_count(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    class Meta:
        model = Course
        fields = ('name', 'image', 'description', 'lesson', 'count')
