from django import forms


class ExtendedSearchForm(forms.Form):
	posted_date = forms.DateField(help_text="Enter a date sometime in the past three months")

