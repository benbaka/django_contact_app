from django.test import Client
from django.test import TestCase

class ContactViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_if_new_contact_url_exist(self):
        response = self.client.get("/contacts/new")
        self.assertEquals(response.status_code, 200)


