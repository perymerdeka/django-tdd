from django.test import TestCase
from django.urls import resolve
from .views import home_page


# Create your tests here.
class UserTest(TestCase):

    def test_fail_math(self):
        self.assertEqual(1 + 1, 3)

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_correct_html(self):
        home = home_page()
        html = home.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<body>HomePage</body>', html)
        self.assertTrue(html.endswith('</html>'))
