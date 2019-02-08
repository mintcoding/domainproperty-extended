from django.urls import path

from . import views

urlpatterns = [
    path('', views.search_domain, name="search_domain"),
    path('', views.index, name="index")
]
