from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, ListView, TemplateView
from .forms import ExtendedSearchForm
import json


class index(FormView):
    template_name = 'extendedsearch/search.html'
    form_class = ExtendedSearchForm

    def post(self, request, *args, **kwargs):
        form = ExtendedSearchForm(request.POST)
        return searchresults(form)


def searchresults(form):
    form_dict = {}
    # if form.is_valid():
    for i in form.visible_fields():
        field_name = i.name
        field_value = i.value()
        form_dict.update({field_name: field_value})
    form_json = json.dumps(form_dict)
    return HttpResponse(form_json, content_type = 'application/json')
