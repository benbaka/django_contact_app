from contacts.models.category import Category
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    age = forms.IntegerField(label="Age", required=True)
    public = forms.BooleanField(label="Public", required=False)
    category = forms.ChoiceField(label="Category", required=False)

    def _populate_category_field(self):
        self.fields['category'].choices = [(category.id, category.name) for category in  Category.objects.filter(owner=self.user_profile)]

    def __init__(self, current_user,  *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.user_profile = current_user.userprofile_set.filter()[0]
        self._populate_category_field()