from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
# from django.template import loader

from .forms import ExtendedSearchForm


def searchresults(request):
    return HttpResponse("searchresults")


def searchdomain(request):
    if request.method == 'POST':
        return "POST"
    else:
        change_date = datetime.date.today() - datetime.timedelta(weeks=3)
        search_form = ExtendedSearchForm(initial={'posted_date': change_date})
        # form_template = loader.get_template('extendedsearch/search.html')
    # context = {
    #     'form': form,
    #
    # }
    #return HttpResponse(template.render(context, request))
    return render(request, 'extendedsearch/search.html', {'search_form': search_form})


def index(request):
    return HttpResponse("Hello world.  You're at the extendedsearch index")
