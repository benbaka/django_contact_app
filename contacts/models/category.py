from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "contacts"

