"""Тесты views приложения gallery."""
import json

from django.test import TestCase
from gallery.models import Image, Group


class CertificateListViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 11 фотоальбомов для тестирования."""
        Image.objects.create(img='image1')
        Image.objects.create(img='image2')
        number_of_album = 11
        for album_num in range(number_of_album):
            Group.objects.create(
                title='title_{}'.format(album_num),
                cover='cover_{}.png'.format(album_num))
            Group.objects.get(id=album_num + 1). \
                items.set(Image.objects.all())

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/galleries/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_2_page(self):
        """Тестирование пагинации 2-ой страницы."""
        resp = self.client.get('/galleries/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertTrue(len(resp.data['results']) == 1)

    def test_page_1(self):
        """Тестирование выводимой информации на 1-ой странице."""
        number_of_album = 10
        image_testlist = [
            {'img': 'http://testserver/change_image_name/image1'},
            {'img': 'http://testserver/change_image_name/image2'}
        ]
        group_testlist = []
        for album_num in range(number_of_album):
            group_testlist.append({
                'title': 'title_{}'.format(album_num),
                'cover': 'http://testserver/change_image_name/cover_{}.png'
                         ''.format(album_num),
                'items': image_testlist})
        resp = self.client.get('/galleries/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 11)
        self.assertEqual(json.loads(resp.content)['results'], group_testlist)
