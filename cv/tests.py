from django.test import TestCase
from cv.models import PersonalDetails, Education


class HomePageTest(TestCase):

    def test_uses_base_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_shows_personal_details(self):
        PersonalDetails.objects.create(name='Joe Bloggs', dob='2000-01-01', email='joe.bloggs@gmail.com')
        response = self.client.get('/cv/')

        self.assertIn('Joe Bloggs', response.content.decode())
        self.assertIn('1 Jan 2000', response.content.decode())
        self.assertIn('joe.bloggs@gmail.com', response.content.decode())


class PersonalDetailsEditTest(TestCase):

    def test_uses_details_edit_template(self):
        response = self.client.get('/cv/personal_details/edit/')
        self.assertTemplateUsed(response, 'cv/details_edit.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/personal_details/edit/', data={'name': 'Joe Bloggs', 'dob': '2000-01-01',
                                                             'email': 'joe.bloggs@gmail.com'})

        self.assertEqual(PersonalDetails.objects.count(), 1)
        my_personal_details = PersonalDetails.objects.first()
        self.assertEqual(my_personal_details.name, 'Joe Bloggs')
        self.assertEqual(str(my_personal_details.dob), '2000-01-01')
        self.assertEqual(my_personal_details.email, 'joe.bloggs@gmail.com')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/personal_details/edit/', data={'name': 'Joe Bloggs', 'dob': '2000-01-01',
                                                                        'email': 'joe.bloggs@gmail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')


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


class EducationNewTest(TestCase):

    def test_uses_details_edit_template(self):
        response = self.client.get('/cv/education/new/')
        self.assertTemplateUsed(response, 'cv/details_edit.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/education/new/', data={'institution': 'My School', 'grades': 'Maths - A',
                                                     'start_date': '2016-09-01', 'end_date': '2018-07-01'})

        self.assertEqual(Education.objects.count(), 1)
        my_education = Education.objects.first()
        self.assertEqual(my_education.institution, 'My School')
        self.assertEqual(my_education.grades, 'Maths - A')
        self.assertEqual(str(my_education.start_date), '2016-09-01')
        self.assertEqual(str(my_education.end_date), '2018-07-01')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/education/new/', data={'institution': 'My School', 'grades': 'Maths - A',
                                                                'start_date': '2016-09-01', 'end_date': '2018-07-01'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')
