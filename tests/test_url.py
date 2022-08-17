from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseTestCase(TestCase):

    def setUp(self) -> None:
        self.home_url = reverse("home")
        self.mylinks_url = reverse("mylinks")

        self.user_data = {
            "email": "test@gmail.com",
            "username": "test",
            "password": "password"
        }
        self.user = User.objects.create_superuser(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.user_data["password"],
        )
        self.client.login(
            username=self.user_data["username"], 
            password=self.user_data["password"]
            )

        self.data = {
            "links_title": "Test",
            "url": "http://example.com"
        }
        self.wrong_data = {
            "links_title": "Test",
            "url": "http://example.com, http://example2.com,"
        }

class URLTestCase(BaseTestCase):

    def test_home_html_rendered(self):
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_mylinks_html_rendered(self):
        response = self.client.get(self.mylinks_url)
        self.assertTemplateUsed(response, "pages/mylinks.html")

    def test_can_create_url(self):
        response = self.client.post(self.home_url, data=self.data)
        self.assertEqual(response.status_code, 302)

    def test_create_url_with_separators(self):
        response = self.client.post(self.home_url, data=self.wrong_data)
        self.assertEqual(response.status_code, 403)
