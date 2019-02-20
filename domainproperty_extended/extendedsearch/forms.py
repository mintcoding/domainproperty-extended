from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ExtendedSearchForm(forms.Form):

    postCode = forms.IntegerField(
        min_value=6000,
        max_value=6999,
        help_text="WA only",
        label="Post code"
    )
    minPrice = forms.IntegerField(
        min_value=1000,
        max_value=2000000,
        help_text="$1000 to $2m",
        label="Min price",
    )
    maxPrice = forms.IntegerField(
        min_value=1000,
        max_value=2000000,
        help_text="$1000 to $2m",
        label="Max price",
    )
    updatedSince = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d'),
        help_text="Optional",
        label="Updated from",
        required=False
    )
    page = forms.IntegerField(
        max_value=10,
        label='page',
        required=False,
        initial=1,
        widget=forms.HiddenInput
    )
    pageSize = forms.IntegerField(
        max_value=100,
        label='pageSize',
        required=False,
        initial=10,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('postCode', css_class='form-group col-4'),
                Column('minPrice', css_class='form-group col-4'),
                Column('maxPrice', css_class='form-group col-4')

            ),
            Row(
                Column('updatedSince', css_class='form-group col-md-auto col-6'),
            ),
            Row(
                Column('page'),
                Column('pageSize'),
            ),
            Submit('submit', 'Search properties')
        )


