from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Housing, Review
from django.views import generic


def main_page(request):
    return render(request, 'main_page.html')


def search_results(request):
    queryset_list = Housing.objects.order_by('-listing_date')

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'search_results.html', context)


class ListingListView(generic.ListView):
    model = Housing
    template_name = 'housing.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Housing.objects.all()


