"""Тесты views приложения recomend."""
import json

from django.test import TestCase
from recomend.models import Recomend


class RecomendListViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 11 рекомендаций для тестирования."""
        number_of_recomend = 11
        for recomend_num in range(number_of_recomend):
            Recomend.objects.create(
                url='url_{}.png'.format(recomend_num),
                title='title_{}'.format(recomend_num),
                year=2001)

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/recomends/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_2_page(self):
        """Тестирование пагинации 2-ой страницы."""
        resp = self.client.get('/recomends/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertTrue(len(resp.data['results']) == 1)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_recomend = 10
        testlist = []
        for recomend_num in range(number_of_recomend):
            testlist.append({
                'url': 'http://testserver/change_image_name/url_{}.png'
                       ''.format(recomend_num),
                'title': 'title_{}'.format(recomend_num),
                'year': '2001 год'})
        resp = self.client.get('/recomends/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertEqual(json.loads(resp.content)['results'], testlist)
