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

def reviews(request):


    return render(request, 'reviews.html')


class ListingListView(generic.ListView):
    model = Housing
    template_name = 'housing.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Housing.objects.all()




def housing_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'map.html', {'mapbox_access_token': mapbox_access_token})


def post(request):
    review_title = request.POST.get('review_title')
    review_description = request.POST.get('review_description')
    if not(review_title and review_description):
        return HttpResponseRedirect(reverse('review'))
    try:
        review = Review(review_title=review_title, review_description=review_description)
        review.save()
    except(KeyError, Review.DoesNotExist):
        return render(request, 'submit_review.html', {
          'error_message': "You did not leave a review."})
    return HttpResponseRedirect(reverse('reviews_list'))


class ReviewsListView(generic.ListView):
    model = Review
    context_object_name = "reviews"
    template_name = 'reviews.html'

    def get_queryset(self):
        return Review.objects.all()

class SubmitReviewView(generic.ListView):
    model = Review
    template_name = 'submit_review.html'