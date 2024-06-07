from django import forms

class CountryForm(forms.Form):
    country = forms.ChoiceField(choices=[], required=True)

    def __init__(self, *args, **kwargs):
        countries = kwargs.pop('countries', [])
        super().__init__(*args, **kwargs)
        self.fields['country'].choices = countries
