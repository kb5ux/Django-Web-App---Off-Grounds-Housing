from django.shortcuts import render
from django.http import HttpResponse
from .models import Housing, Review
from django.views import generic


def index(request):
    return HttpResponse("Welcome to the Off-grounds Housing Website!")


class ListingListView(generic.ListView):
    model = Housing
    template_name = 'housing.html'


