from rest_framework import serializers

from main.models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
