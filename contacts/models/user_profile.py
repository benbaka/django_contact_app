from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True)

    class Meta:
        app_label = "contacts"