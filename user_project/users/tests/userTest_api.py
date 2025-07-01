from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models.user import User, Address, Geo, Company

class UserApiTests(APITestCase):

    def setUp(self):
        self.geo = Geo.objects.create(lat='12.34', lng='56.78')
        self.address = Address.objects.create(
            street='Test Street',
            suite='Suite 100',
            city='Test City',
            zipcode='12345',
            geo=self.geo
        )
        self.company = Company.objects.create(name='Test Company')
        self.user = User.objects.create(
            name='Test User',
            username='testuser',
            email='test@example.com',
            phone='1234567890',
            website='https://example.com',
            address=self.address,
            company=self.company
        )

    def test_get_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        if isinstance(data, dict) and 'results' in data:
            users = data['results']
        else:
            users = data

        self.assertIsInstance(users, list)
        self.assertTrue(any(u['id'] == self.user.id for u in users))

    def test_get_user_detail(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)
