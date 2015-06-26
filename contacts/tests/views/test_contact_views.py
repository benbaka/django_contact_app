from django.test import Client
from django.test import TestCase

class ContactViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_access_contact_url(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_should_return_list_of_contacts_in_context(self):
        response = self.client.get('/contacts/')
        self.assertIn('contacts', response.context)
        self.assertTrue(type(response.context['contacts']), dict) 

    def test_should_get_the_index_page_form_contacts_url(self):
        response = self.client.get('/contacts/')
        self.assertTemplateUsed(response, 'contacts/index.html')

