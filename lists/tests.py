from django.test import TestCase
from django.urls import resolve

from .views import home_page


# Create your tests here.
class UserTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_using_templates(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'lists/index.html')
