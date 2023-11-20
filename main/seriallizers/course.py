from rest_framework import serializers

from main.models import Course, Amount


class CourseSerializer(serializers.ModelSerializer):
    last_amount = serializers.IntegerField(source='amount_set.all.first.amount')

    class Meta:
        model = Course
        fields = '__all__'
