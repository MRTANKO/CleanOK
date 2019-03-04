"""Тесты views приложения news."""
import json
from datetime import date

from django.test import TestCase
from news.models import News


class NewsViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 11 новостей для тестирования."""
        number_of_news = 11
        for news_num in range(number_of_news):
            News.objects.create(
                date=date(year=2019, month=2, day=1 + news_num),
                title='Title__{}'.format(news_num),
                preview='Preview__{}'.format(news_num),
                text='Text__{}'.format(news_num))
        for number in range(2, 5):
            News.objects.get(id=number).related.set([3 + number])

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_page_2(self):
        """Тестирование пагинации 2-ой страницы."""
        resp = self.client.get('/news/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertTrue(len(resp.data['results']) == 1)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_news = 10
        testlist = []
        for news_num in range(number_of_news):
            testlist.append({
                'id': news_num + 1,
                'date': str(date(year=2019, month=2, day=1 + news_num)),
                'title': 'Title__{}'.format(news_num),
                'preview': 'Preview__{}'.format(news_num),
                'text': 'Text__{}'.format(news_num),
                'related': []})
        for number in range(2, 5):
            testlist[number - 1]['related'] = [3 + number]
            testlist[2 + number]['related'] = [number]
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertEqual(json.loads(resp.content)['results'], testlist)
