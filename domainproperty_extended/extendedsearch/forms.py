from django import forms




class ExtendedSearchForm(forms.Form):
    # posted_date = forms.DateField(help_text="Enter a date sometime in the past three months", input_formats=['%d/%m/%Y %H:%M'])
    posted_date = forms.DateField(input_formats=['%d/%m/%Y %H:%M'])
    property_types = forms.CheckboxSelectMultiple()
    minimum_price = forms.IntegerField()
