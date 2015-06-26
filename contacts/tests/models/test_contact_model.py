from django.test import TestCase
from contacts.models import Contact


class ContactTestCase(TestCase):
    def setUp(self):
        pass

    def test_should_save_partial_contact(self):
        contact = Contact()
        contact.name = "ben"
        contact.email_address = "brainychip.gmail.com"
        contact.save()
        self.assertEqual(Contact.objects.count(), 1)

    def test_should_save_an_invalid_model(self):
        contact = Contact()
        contact.save()
        self.assertTrue(Contact.objects.count(), 1)

