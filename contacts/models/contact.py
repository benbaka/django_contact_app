from contacts.models.user_profile import UserProfile
from django.db import models

GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        )
class Contact(models.Model):
    name = models.CharField(max_length= 255)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=GENDER, null=True) 
    school = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length= 255, null=True)
    email_address = models.EmailField(null=True)
    owner = models.ForeignKey(UserProfile, null=True)
    public = models.BooleanField(default=False)


    class Meta:
        app_label = "contacts"

