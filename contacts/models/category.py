from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        app_label = "contacts"

