from django.urls import path

from . import views

urlpatterns = [
    path('searchresults/', views.searchresults, name="searchresults"),
    # path('searchdomain/', views.searchdomain),
    path('', views.index.as_view(), name="index"),
]
