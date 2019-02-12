from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from .forms import ExtendedSearchForm
from . import auth


class SearchForm(FormView):
    template_name = 'extendedsearch/search.html'
    form_class = ExtendedSearchForm

    def post(self, request, *args, **kwargs):

        form = ExtendedSearchForm(request.POST)
        querydata = parse_query_data(form)
        request_auth = auth.Auth()
        request_auth.clientid, request_auth.clientpass = request_auth.retrieve_credentials()

        response_data = request_auth.retrieve_approved_data(querydata)
        context = {
            'response_data': response_data
        }
        return render(request, template_name='extendedsearch/searchresults.html', context=context)


def parse_query_data(form):

    querydata = {
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

    form_dict = {
        "locations": [
            {
                "state": "WA",
                "postCode": "",
            }
        ]
    }
    # if form.is_valid():
    for i in form.visible_fields():
        field_name = i.name
        field_value = i.value()
        if i.name == "postCode":
            form_dict['locations'][0].update({'postCode': field_value})
        else:
            form_dict.update({field_name: field_value})

    querydata.update(form_dict)

    return querydata
