from rest_framework.generics import CreateAPIView, ListAPIView

from main.models import Amount
from main.seriallizers.amount import AmountSerializer


class AmountCreateView(CreateAPIView):
    serializer_class = AmountSerializer


class AmountListView(ListAPIView):
    queryset = Amount.objects.all()
    serializer_class = AmountSerializer
