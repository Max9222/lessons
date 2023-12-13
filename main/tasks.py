from itertools import count

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from main.models import Course, Subscription


@shared_task
def send_massage_add_materials(course_id):

    course = Course.objects.get(pk=course_id)  # get вместо filter
    subscriptions = Subscription.objects.filter(course=course_id)
    for a in subscriptions:
        print(a.user)

        #print('Письмо отправлено')
        # send_mail(
        #     subject='Новость',
        #     message='Появились новые материалы к Курсе',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[settings.EMAIL_MODERATOR]
        # )
