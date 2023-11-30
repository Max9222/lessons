from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from main.models import Subscription
# from main.permissions.lesson import *
from main.seriallizers.subscription import SubscriptionSerializers

class SubscriptionCreateView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers
    # permission_classes = [IsAuthenticated]

class SubscriptionDestroyView(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

# class SubscriptionListView(ListAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializers
#     # permission_classes = [IsAuthenticated]


# class SubscriptionRetrieveView(RetrieveAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializers
#     permission_classes = [IsAuthenticated, IsModerator | IsOwner]

# class SubscriptionUpdateView(UpdateAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializers
#     permission_classes = [IsAuthenticated, IsModerator | IsOwner]
