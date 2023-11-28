from rest_framework import serializers

from main.models import Lesson
from main.validators.lesson import YouTubeValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeValidator(field='link')]
