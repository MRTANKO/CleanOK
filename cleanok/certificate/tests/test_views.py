"""Тесты views приложения certificate."""
import json

from django.test import TestCase
from certificate.models import Certificate


class CertificateListViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 11 сертификатов для тестирования."""
        number_of_certificate = 11
        for certificate_num in range(number_of_certificate):
            Certificate.objects.create(
                url='picture%s.png' % certificate_num,
                title='title%s' % certificate_num,
                subt='company%s' % certificate_num)

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/certificates/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_2_page(self):
        """Тестирование пагинации 2-ой страницы."""
        resp = self.client.get('/certificates/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertTrue(len(resp.data['results']) == 1)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_certificate = 10
        testlist = []
        for certificate_num in range(number_of_certificate):
            testlist.append({
                'url': 'http://testserver/change_image_name/picture%s.png'
                       % certificate_num,
                'title': 'title%s' % certificate_num,
                'subt': 'company%s' % certificate_num})
        resp = self.client.get('/certificates/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertEqual(json.loads(resp.content)['results'], testlist)
