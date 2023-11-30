from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from main.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """ Тестируем создание уроков """
        data = {
            'id': 1,
            "name": "Видео_1",
            "description": "Язык 1",
            "image": '',
            "link": "https://www.youtube.com/",
            "is_public": True,
            "lesson_owner": ''
        }
        response = self.client.post(
            reverse("main:lesson_create"),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'Видео_1', 'description': 'Язык 1', 'image': None, 'link': 'https://www.youtube.com/',
             'is_public': True, 'lesson_owner': None}
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ Тестируем вывод списка уроков """
        data = {
            "count": 5,
            "next": '',
            "previous": '',
            "results": [
                {
                    "id": 1,
                    "name": "Python",
                    "description": "Чзык №1",
                    "image": '',
                    "link": '',
                    "is_public": False,
                    "lesson_owner": ''
                },
                {
                    "id": 2,
                    "name": "C++",
                    "description": "Чзык №2",
                    "image": '',
                    "link": '',
                    "is_public": False,
                    "lesson_owner": ''
                },
            ]
        }
        response = self.client.get(
            reverse("main:lesson_list"),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_lesson(self):
        """ Тестируем вывод одного урока """
        data = {
            "id": 1,
            "name": "Python",
            "description": "Чзык №1",
            "image": '',
            "link": '',
            "is_public": False,
            "lesson_owner": ''
        }

        response = self.client.get(

            reverse("main:lesson_detail", args=[self.lesson.pk]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """ Тестируем удаление урока """
        response = self.client.delete(reverse("main:lesson_delete", args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
