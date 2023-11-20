from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='main/', verbose_name='превью(картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')

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
    link = models.SlugField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)


class Amount(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    amount = models.PositiveIntegerField(verbose_name='количество уроков')

    def __str__(self):
        return f'{self.course} - {self.lesson} - {self.amount}'

    class Meta:
        verbose_name = 'кол-во уроков'
        verbose_name_plural = 'кол-во уроков'
        ordering = ('-amount',)
