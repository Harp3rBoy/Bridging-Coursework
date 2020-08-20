from django.test import TestCase
from django.urls import resolve
from cv.views import home_page


class HomePageTest(TestCase):

    def test_cv_url_resolves_to_home_page_view(self):
        found = resolve('/cv')
        self.assertEqual(found.func, home_page)
