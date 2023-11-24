from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import OrderingFilter
from main.models import Payments
from main.seriallizers.payments import PaymentsSerializer


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_payment', 'lesson_payment', 'payment_method')
    ordering_fields = ('date_of_payment',)

class PaymentsCreateView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class PaymentsRetrieveView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class PaymentsUpdateView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class PaymentsDestroyView(DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
