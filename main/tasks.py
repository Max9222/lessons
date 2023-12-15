from itertools import count

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from main.models import Course, Subscription


@shared_task
def send_massage_add_materials(course_id):
    """Отложенная задача - рассылка на обновления материалов курса"""

    course = Course.objects.get(pk=course_id)
    subscriptions = Subscription.objects.filter(course=course_id)
    for a in subscriptions:
        send_mail(
            subject=f"{course.description}",
            message=f"Появились новые материалы к {course.description}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_MODERATOR]
        )
