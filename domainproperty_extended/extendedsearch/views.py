from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from django.views.generic import FormView, CreateView, ListView, TemplateView
from .forms import ExtendedSearchForm
from bootstrap4 import bootstrap

def searchresults(request):
    return HttpResponse("searchresults")


# def index(request):
#     if request.method == 'POST':
#         return "POST"
#     else:
#         change_date = datetime.date.today() - datetime.timedelta(weeks=3)
#         # search_form = ExtendedSearchForm(initial={'posted_date': change_date})
#         search_form = ExtendedSearchForm()
#     return render(request, 'extendedsearch/search.html', {'search_form': search_form})
#
# def index(request):
#     change_date = datetime.date.today() - datetime.timedelta(weeks=3)
#     # search_form = ExtendedSearchForm(initial={'posted_date': change_date})
#     search_form = ExtendedSearchForm()
#     # return render(request, 'extendedsearch/search.html', {'search_form': search_form})
#     return render(request, 'extendedsearch/search.html')

class index(FormView):
    template_name = 'extendedsearch/search.html'
    form_class = ExtendedSearchForm
    def post(self, request, *args, **kwargs):
        return HttpResponse("form sent")


# class ExtSearch(CreateView):
#     template_name = 'extendedsearch/search.html'
#     form_class = ExtendedSearchForm
#
    # def index(self, request):
    #     if request.method == 'POST':
    #         return HttpResponse("POST")
    #     else:
    #         change_date = datetime.date.today() - datetime.timedelta(weeks=3)
    #         # search_form = ExtendedSearchForm(initial={'posted_date': change_date})
    #         # search_form = ExtendedSearchForm()
    #     return render(request, 'extendedsearch/search.html')
