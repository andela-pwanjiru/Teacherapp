from django.test import TestCase
from mwalimu.models import User


class TeacherAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user', password='password')

    def test_user_signup(self):
        self.assertEqual(self.user.get_username(), 'user')
        self.assertIsInstance(self.user, User)


