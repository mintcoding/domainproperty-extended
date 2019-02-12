from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ExtendedSearchForm(forms.Form):

    postCode = forms.IntegerField(
        min_value=6000,
        max_value=6999,
        label="Post code"
    )
    minPrice = forms.IntegerField(
        min_value=10000, max_value=2000000,
        label="Minimum price",
    )
    maxPrice = forms.IntegerField(
        min_value=10000, max_value=2000000,
        label="Maximum price",
    )
    inspectionFrom = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text="Pick a date sometime within the past three months",
        label="Earliest inspection",
        required=False
    )
    inspectionTo = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        help_text="Pick a date sometime within the past three months",
        label="Latest inspection",
        required=False
    )

