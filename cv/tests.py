from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_base_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv/base.html')
