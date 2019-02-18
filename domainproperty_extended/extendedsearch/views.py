from django.shortcuts import render
from django.views.generic import FormView
from .forms import ExtendedSearchForm
from . import domainapi
from django.core.validators import ValidationError


class SearchForm(FormView):
    # Request.session is called in the GET and POST methods to ensure search result isolation per browser session
    template_name = 'extendedsearch/search.html'
    form_class = ExtendedSearchForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.querydata = {
            "listingType": "Sale",
            "minPrice": "",
            "maxPrice": "",
            "locations": [
                {
                    "state": "WA",
                    "postCode": "",
                }
            ]
        }
        self.form_dict = {
            "locations": [
                {
                    "state": "WA",
                    "postCode": "",
                }
            ],
            "page": 1,
            "pageSize": 10,
        }

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            self.parse_form_data(form)
            response_data = get_response_data(self.querydata)
            context = {
                'response_data': response_data
            }

            request.session['querydata'] = self.querydata
            return render(request, template_name='extendedsearch/searchresults.html', context=context)
        else:
            raise ValidationError(form.errors)

    def get(self, request, *args, **kwargs):
        if request.GET.get('page'):
            # Overridden GET method adds a conditional to take 'page' parameter (if it exists) and update
            # query_data dict for the get_response_data method,
            # retaining user search criteria persisting in that browser session.
            # Should no 'page' parameter exist, extendedsearch form is returned
            query_data = request.session['querydata']
            query_data.update({'page': request.GET.get('page')})
            response_data = get_response_data(query_data)
            context = {
                'response_data': response_data
            }

            return render(request, template_name='extendedsearch/searchresults.html', context=context)
        else:
            return self.render_to_response(self.get_context_data())

    def parse_form_data(self, form):
        # Method must run every time a user sets search criteria via the extendedsearch form
        for i in form.visible_fields():
            field_name = i.name
            field_value = i.value()
            if i.name == "postCode":
                try:
                    self.form_dict['locations'][0].update({'postCode': field_value})
                except (ValueError, Exception) as e:
                    raise e
            else:
                try:
                    self.form_dict.update({field_name: field_value})
                except (ValueError, Exception) as e:
                    raise e
        try:
            self.querydata.update(self.form_dict)
        except (ValueError, Exception) as e:
            raise e


def get_response_data(query_data):
    # Interacts with the Domain API to receive approved data according to the query_data dict request
    request_auth = domainapi.DomainApi()
    request_auth.retrieve_credentials()
    response_data = request_auth.retrieve_approved_data(query_data)

    return response_data
