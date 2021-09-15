from django.test import TestCase
from django.urls import resolve
from .views import home_page
from django.http import HttpRequest


# Create your tests here.
class UserTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_correct_html(self):
        request = HttpRequest()
        home = home_page(request)
        html = home.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<body>HomePage</body>', html)
        self.assertTrue(html.endswith('</html>'))
