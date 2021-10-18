from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.

class GoogleLogin(TestCase):
    def test_ValidUser(self):
        self.c = Client()
        self.user = User.objects.create(username='test', password='123')
        self.user.set_password('456')
        self.user.save()
        self.user = authenticate(username='test', password='456')
        login = self.c.login(username='test', password='456')
        self.assertTrue(login)

    def test_InvalidUser(self):
        self.c = Client()
        self.user = User.objects.create(username='test', password='123')
        self.user.set_password('456')
        self.user.save()
        self.user = authenticate(username='test', password='456')
        login = self.c.login(username='test', password='123')
        self.assertFalse(login)
