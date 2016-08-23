from django.core.urlresolvers import reverse
from django.test import TestCase
from mwalimu.models import User


class TeacherAppViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Penny', password='password')

    def test_user_login(self):
        response = self.client.post(self.user, reverse('login'))
        self.assertEquals(response.status_code, 200)
