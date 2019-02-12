from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ExtendedSearchForm(forms.Form):

    postCode = forms.IntegerField(
        min_value=6000,
        max_value=6999,
        help_text="WA postcodes only",
        label="Post code"
    )
    minPrice = forms.IntegerField(
        min_value=1000,
        max_value=2000000,
        help_text="Range: $1000 to $2,000,000",
        label="Minimum price",
    )
    maxPrice = forms.IntegerField(
        min_value=1000,
        max_value=2000000,
        help_text="Range: $1000 to $2,000,000",
        label="Maximum price",
    )
    updatedSince = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d'),
        help_text="Optional",
        label="Listing updated from",
        required=False
    )
    inspectionFrom = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d'),
        help_text="Optional",
        label="Earliest inspection",
        required=False
    )
    inspectionTo = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d'),
        help_text="Optional",
        label="Latest inspection",
        required=False
    )
