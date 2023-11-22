from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {'user': 'admin', 'date_of_payment': '2023-10-14T10:28:58.644Z', 'course_payment': 'null', 'lesson_payment': 'null', 'payment_amount': 100, 'payment_method': 'CARD'}
        ]
