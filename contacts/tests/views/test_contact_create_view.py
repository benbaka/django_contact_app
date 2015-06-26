from django.test import Client
from django.test import TestCase

class ContactViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_return_new_contact_form(self):
        response = self.client.get("/contact/new")
        self.assertEquals(response.status_code, 200)


