"""Тесты views приложения feedback."""
import json

from django.contrib.auth.models import User
from django.test import TestCase
from feedback.models import Message


class FeedbackListViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Регистрация пользователя."""
        User.objects.create_superuser(
            username='vlad',
            email='sadsd@mail.ru',
            password='1234qwer')

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        self.client.login(username='vlad', password='1234qwer')
        resp = self.client.get('/feedbacks/')
        self.assertEqual(resp.status_code, 200)

    def test_posts(self):
        """Тестирование post запроса."""
        self.client.post('/feedbacks/', {
            'first_name': 'user',
            'last_name': 'last',
            'message': 'test'})
        self.assertEqual(Message.objects.get(id=1).first_name, 'user')
        self.assertEqual(Message.objects.get(id=1).last_name, 'last')
        self.assertEqual(Message.objects.get(id=1).message, 'test')

    def test_pagination_1_page(self):
        """Тестирование пагинации 1 страницы get запроса."""
        number_of_feedback = 10
        for feedback_num in range(number_of_feedback):
            self.client.post('/feedbacks/', {
                'first_name': 'user_{}'.format(feedback_num),
                'last_name': 'last_{}'.format(feedback_num),
                'message': 'test_{}'.format(feedback_num)})
        self.client.login(username='vlad', password='1234qwer')
        resp = self.client.get('/feedbacks/?page=1')
        self.assertEqual(resp.status_code, 200)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_feedback = 10
        testlist = []
        for feedback_num in range(number_of_feedback):
            self.client.post('/feedbacks/', {
                'first_name': 'user_{}'.format(feedback_num),
                'last_name': 'last_{}'.format(feedback_num),
                'message': 'test_{}'.format(feedback_num)})

            testlist.append({
                'id': feedback_num + 1,
                'first_name': 'user_{}'.format(feedback_num),
                'last_name': 'last_{}'.format(feedback_num),
                'message': 'test_{}'.format(feedback_num)
            })
        self.client.login(username='vlad', password='1234qwer')
        resp = self.client.get('/feedbacks/?page=1')
        self.assertEqual(json.loads(resp.content)['results'], testlist)
