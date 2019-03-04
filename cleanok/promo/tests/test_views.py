"""Тесты views приложения promo."""
import json
from datetime import date

from django.test import TestCase
from promo.models import Promo


class PromoListViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 11 акций для тестирования."""
        number_of_promo = 11
        for promo_num in range(number_of_promo):
            Promo.objects.create(
                title='title_{}'.format(promo_num),
                preview='preview_{}'.format(promo_num),
                date=date(year=2019, month=2, day=1 + promo_num))

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/promos/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_2_page(self):
        """Тестирование пагинации 2-ой страницы."""
        resp = self.client.get('/promos/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertTrue(len(resp.data['results']) == 1)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_promo = 10
        testlist = []
        for promo_num in range(number_of_promo):
            testlist.append({
                'id': promo_num + 1,
                'date': str(date(year=2019, month=2, day=1 + promo_num)),
                'title': 'title_{}'.format(promo_num),
                'preview': 'preview_{}'.format(promo_num)})
        resp = self.client.get('/promos/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertEqual(json.loads(resp.content)['results'], testlist)
