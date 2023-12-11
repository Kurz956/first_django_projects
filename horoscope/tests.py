from django.test import TestCase
from . import views

# Create your tests here.

class TestHoroscope(TestCase):
    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_sign(self):
        for sign, description in views.zodiac_signs.items():
            response = self.client.get(f'/horoscope/{sign}/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(f'{description._description}',
                          response.content.decode())


    def test_sign_redirect(self):
        for sign, description in views.zodiac_signs.items():
            response = self.client.get(f'/horoscope/{description._index}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{sign}/')