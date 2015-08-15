from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    age = forms.IntegerField(label="Age", required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
