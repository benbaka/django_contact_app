from django.test import Client
from django.test import TestCase
from contacts.forms.contact_form import ContactForm
class ContactFormTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_if_empty_contact_form_is_valid(self):
        form = ContactForm({})
        self.assertFalse(form.is_valid())


