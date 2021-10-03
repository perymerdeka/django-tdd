from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string

from .views import home_page


# Create your tests here.
class UserTest(TestCase):

    def test_using_templates(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'lists/index.html')

    def test_correct_html(self):
        request: HttpRequest = HttpRequest()
        response: HttpResponse = home_page(request)
        html_page = response.content.decode('utf-8')
        expect_html: str = render_to_string('lists/index.html')
        self.assertEqual(html_page, expect_html)

    # testing post request
    def test_save_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
