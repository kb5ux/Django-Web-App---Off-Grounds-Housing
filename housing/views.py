from django.db.models import Avg
from django.shortcuts import render, redirect
from django.http import  HttpResponseRedirect
from django.urls import reverse

from .forms import ReviewForm
from .models import Listing, Review
from django.views import generic


def home_page(request):
    return render(request, 'home_page.html')


def search_results(request):
    queryset_list = Listing.objects.order_by('-listing_date')

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
    model = Listing
    template_name = 'housing.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.all()


def housing_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'map.html', {'mapbox_access_token': mapbox_access_token})


def add_Review(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.description = request.POST["description"]
            data.rating = request.POST["rating"]
            data.listing = listing
            data.save()
            return redirect("listing_details", id)
        else:
            form = ReviewForm()
        context = {
            "form": form,
            "listing": listing,
            "reviews": form,
        }
    return render(request, 'listing_details.html', context)


def ListingDetails(request, id):
    listing = Listing.objects.get(id=id)
    reviews = Review.objects.filter(listing=id).order_by("-description")
    average_rating = reviews.aggregate(Avg("rating" ))["rating__avg"]

    if average_rating is None:
        average_rating = 0
    average_rating = round(average_rating, 2)
    context = {
        "listing": listing,
        "reviews": reviews,
        "average_rating": average_rating
    }
    return render(request, 'listing_details.html', context)





