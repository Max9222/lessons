from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='main/', verbose_name='превью(картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    lesson = models.ForeignKey('main.Lesson', verbose_name='Урок', related_name='main', on_delete=models.SET_NULL, null=True)
    course_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                     verbose_name='владелец курса')
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='main/', verbose_name='превью(картинка)', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    lesson_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='владелец урока')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)


class Payments(models.Model):
    CARD = 'Card'
    TRANSFER = 'Transfer'

    PAYMENT_METHOD_CHOICES = (
        (CARD, 'Card'),
        (TRANSFER, 'Transfer'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='main', null=True)
    #user = models.CharField(max_length=100, verbose_name='пользователь')
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course_payment = models.ForeignKey('main.Course', on_delete=models.SET_NULL, null=True)
    lesson_payment = models.ForeignKey('main.Lesson', on_delete=models.SET_NULL, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES, default=CARD, verbose_name='способы оплаты')

    def __str__(self):
        return f"Оплата от {self.user} для {self.course_payment if self.course_payment else self.lesson_payment}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('date_of_payment',)
