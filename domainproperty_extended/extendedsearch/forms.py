from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ExtendedSearchForm(forms.Form):
    first_posted_date = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text="Pick a date sometime within the past three months",
    )
    last_posted_date = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text="Pick a date sometime within the past three months",
    )
    property_types = forms.CheckboxSelectMultiple()
    minimum_price = forms.IntegerField(min_value=10000, max_value=2000000)
