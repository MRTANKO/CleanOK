"""Тесты views приложения services."""
import json

from django.test import TestCase
from services.models import Service, Item, Category
from django.contrib.auth.models import User


class ServiceViewTest(TestCase):
    """Класс для тестирования views."""

    @classmethod
    def setUpTestData(cls):
        """Создание 12 сервисов для теста."""
        User.objects.create_superuser(
            username='vlad',
            email='sadsd@mail.ru',
            password='1234qwer')
        Item.objects.create(name='Item_1')
        Item.objects.create(name='Item_2')
        Category.objects.create(name='Category_1')
        Category.objects.create(name='Category_2')
        number_of_services = 5
        for services_num in range(number_of_services):
            Service.objects.create(
                category=Category.objects.get(id=1),
                name='Service__{}'.format(services_num),
                desc='Desc__{}'.format(services_num),
                price=services_num,
                note='Note__{}'.format(services_num),
                warn='Warn__{}'.format(services_num)
            )
        number_of_services = 7
        for services_num in range(number_of_services):
            Service.objects.create(
                category=Category.objects.get(id=2),
                name='Service__{}'.format(services_num),
                desc='Desc__{}'.format(services_num),
                price=services_num,
                note='Note__{}'.format(services_num),
                warn='Warn__{}'.format(services_num)
            )
            Service.objects.get(
                id=services_num + 6
            ).items.set(
                Item.objects.all()
            )

    def test_view_url_exists_at_desired_location(self):
        """Тестирование url."""
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/services/categories/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination(self):
        """Тестирование пагинаций."""
        resp = self.client.get('/services/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 12)
        self.assertTrue(len(resp.data['results']) == 2)
        resp = self.client.get('/services/?page=1')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 12)
        self.assertTrue(len(resp.data['results']) == 10)
        resp = self.client.get('/services/categories/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.data['count'] == 2)
        self.assertTrue(len(resp.data['results']) == 2)

    def test_page(self):
        """Тестирование выводимой информации на страницах get."""
        testlist = []
        number_of_services = 5
        for services_num in range(number_of_services):
            testlist.append({
                'id': services_num + 1,
                'category': {'id': 1, 'name': 'Category_1'},
                'name': 'Service__{}'.format(services_num),
                'desc': 'Desc__{}'.format(services_num),
                'items': [],
                'price': 'От {} рублей'.format(services_num),
                'note': 'Note__{}'.format(services_num),
                'warn': 'Warn__{}'.format(services_num)
            })
        number_of_services = 5
        for services_num in range(0, number_of_services):
            testlist.append({
                'id': services_num + 6,
                'category': {'id': 2, 'name': 'Category_2'},
                'name': 'Service__{}'.format(services_num),
                'desc': 'Desc__{}'.format(services_num),
                'items': [{'id': 1, 'name': 'Item_1'},
                          {'id': 2, 'name': 'Item_2'}],
                'price': 'От {} рублей'.format(services_num),
                'note': 'Note__{}'.format(services_num),
                'warn': 'Warn__{}'.format(services_num)
            })
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.content)['results'], testlist)

        testlist = [
            {'id': 1, 'name': 'Category_1', 'items': []},
            {'id': 2, 'name': 'Category_2', 'items': []}
        ]
        number_of_services = 5
        for services_num in range(number_of_services):
            testlist[0]['items'].append({
                'id': services_num + 1,
                'name': 'Service__{}'.format(services_num)
            })
        number_of_services = 7
        for services_num in range(number_of_services):
            testlist[1]['items'].append({
                'id': services_num + 6,
                'name': 'Service__{}'.format(services_num)
            })
        resp = self.client.get('/services/categories/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.content)['results'], testlist)

    def test_post(self):
        """Тестирование выводимой информации на страницах post."""
        testlist = []
        number_of_request = 9
        for request_num in range(number_of_request):
            self.client.post('/services/leads/', {
                'name': 'User__{}'.format(request_num),
                'phone': '892421645{}'.format(request_num),
                'service': 1,
                'comment': 'Comment__{}'.format(request_num)
            })
            testlist.append({
                'id': request_num + 1,
                'name': 'User__{}'.format(request_num),
                'phone': '892421645{}'.format(request_num),
                'service': {'id': 1, 'name': 'Service__0'},
                'comment': 'Comment__{}'.format(request_num)
            })
        self.client.login(username='vlad', password='1234qwer')
        resp = self.client.get('/services/leads/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.content)['results'], testlist)
