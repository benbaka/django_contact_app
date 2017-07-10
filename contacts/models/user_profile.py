from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True)

    class Meta:
        app_label = "contacts"

    def __unicode__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)