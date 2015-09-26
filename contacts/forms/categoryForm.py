from contacts.models.category import Category
from django.forms.models import ModelForm


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

