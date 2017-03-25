from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = ('contact_name', 'contact_email', 'comment')
