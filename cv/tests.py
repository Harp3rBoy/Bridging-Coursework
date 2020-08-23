from django.test import TestCase
from cv.models import Item
from cv.models import PersonalDetails

class HomePageTest(TestCase):

    def test_uses_base_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv/base.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/cv')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class PostEditTest(TestCase):

    def test_uses_post_edit_template(self):
        response = self.client.get('/cv/edit_post')
        self.assertTemplateUsed(response, 'cv/details_edit.html')


class PersonalDetailsModelTest(TestCase):

    def test_making_and_saving_model(self):
        personal_details = PersonalDetails()
        personal_details.name = 'Joe Bloggs'
        personal_details.dob = '2000-01-01'
        personal_details.email = 'joe.bloggs@gmail.com'
        personal_details.save()

        saved_details = PersonalDetails.objects.all()
        self.assertEqual(saved_details.count(), 1)

        my_personal_details = saved_details[0]
        self.assertEqual(my_personal_details.name, 'Joe Bloggs')
        self.assertEqual(str(my_personal_details.dob), '2000-01-01')
        self.assertEqual(my_personal_details.email, 'joe.bloggs@gmail.com')
