from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import datetime
from django.urls import reverse

from .forms import ExtendedSearchForm

def search_domain(request):
    if request.method == 'POST':
        return "POST"
    else:
        change_date = datetime.date.today() - datetime.timedelta(weeks=3)
        form = ExtendedSearchForm(initial={'posted_date': change_date})

    context = {
        'form': form,

    }
    return render(request, 'extendedsearch/search_domain', context)


def index(request):
    return HttpResponse("Hello world.  You're at the extendedsearch index")
