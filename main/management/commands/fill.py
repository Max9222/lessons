from django.core.management import BaseCommand
from main.models import Payments


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {
                "id": 1,
                "user": "1",
                "date_of_payment": "2023-11-24T16:45:48.951812Z",
                "payment_amount": "100.00",
                "payment_method": "Card",
                "course_payment": 1,
                "lesson_payment": 1
            },
            {
                "id": 2,
                "user": "2",
                "date_of_payment": "2023-11-24T16:46:31.784079Z",
                "payment_amount": "200.00",
                "payment_method": "Transfer",
                "course_payment": 1,
                "lesson_payment": 2
            }
        ]

        for payments_list in payments_list:
            Payments.objects.create(**payments_list)
