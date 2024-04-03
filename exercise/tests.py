from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import User


class NetElementTestCase(APITestCase):
    """
    Тестирование для модели Элементо Сети
    """
    def setUp(self):
        self.user = User.objects.create(
            email='test1@yandex.ru',
            password='test12345'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_exercise_create(self):

        # Создание сущности модели Упражнения
        data_0 = {
            "name": "test_0",
            "description": "test_0",
            "exercise_type": "Statics",
            "difficulty_level": "Advanced",
            "duration": "00:15:00",
            "approaches": 5,
            "repetition": 5
        }
        response = self.client.post(
            reverse('exercise:exercise_create'),
            data=data_0
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Создание сущности модели Упражнения с количеством подходов 0
        data_1 = {
            "name": "test_1",
            "description": "test_1",
            "exercise_type": "Statics",
            "difficulty_level": "Advanced",
            "duration": "00:15:00",
            "approaches": 0,
            "repetition": 5
        }
        response = self.client.post(
            reverse('exercise:exercise_create'),
            data=data_1
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # Создание сущности модели Упражнения с количеством повторений 0
        data_2 = {
            "name": "test_2",
            "description": "test_2",
            "exercise_type": "Statics",
            "difficulty_level": "Advanced",
            "duration": "00:15:00",
            "approaches": 5,
            "repetition": 0
        }
        response = self.client.post(
            reverse('exercise:exercise_create'),
            data=data_2
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # Создание сущности модели Упражнения с временем на выполнение равным нулю
        data_3 = {
            "name": "test_3",
            "description": "test_3",
            "exercise_type": "Statics",
            "difficulty_level": "Advanced",
            "duration": "00:00:00",
            "approaches": 5,
            "repetition": 5
        }
        response = self.client.post(
            reverse('exercise:exercise_create'),
            data=data_3
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
