from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from .forms import ExtendedSearchForm
from . import auth, view_utils
from django.core.validators import ValidationError


class SearchForm(FormView):
    template_name = 'extendedsearch/search.html'
    form_class = ExtendedSearchForm

    def post(self, request, *args, **kwargs):

        form = ExtendedSearchForm(request.POST)
        if form.is_valid():
            querydata = view_utils.parse_query_data(form)
            request_auth = auth.Auth()
            request_auth.clientid, request_auth.clientpass = request_auth.retrieve_credentials()

            response_data = request_auth.retrieve_approved_data(querydata)
            context = {
                'response_data': response_data
            }
            return render(request, template_name='extendedsearch/searchresults.html', context=context)
        else:
            raise ValidationError(form.errors)
