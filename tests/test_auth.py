from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class BaseTestCase(TestCase):

    def setUp(self) -> None:
        self.register_url = reverse('signup')
        self.user = {
            "email": "test1@gmail.com", 
            "username": "test1",
            "password": "password", 
            "password2": "password"
            }

        self.user_short_pass = {
            "email": "test2@gmail.com", 
            "username": "test2",
            "password": "pass", 
            "password2": "passw"}

class RegisterTestCase(BaseTestCase):

    def test_can_register_user(self):
        response = self.client.post(self.register_url, data=self.user)
        self.assertEqual(response.status_code, 302)
    
    def test_cant_register_with_shortpass(self):
        with self.assertRaises(KeyError):
            self.client.post(self.register_url, self.user_short_pass)
    
    def test_cant_register_with_already_taken_email(self):
        self.client.post(self.register_url, self.user)
        with self.assertRaises(IntegrityError):
            self.client.post(self.register_url, self.user)