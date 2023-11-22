from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='main/', verbose_name='превью(картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    lesson = models.ForeignKey('main.Lesson', verbose_name='Урок', related_name='main', on_delete=models.SET_NULL, null=True)

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

    #course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)
