from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Housing, Review
from django.views import generic

def index(request):
  return render(request, 'main_page.html')


# Class-based list view for the Housing model

class ListingListView(generic.ListView):
    model = Housing
    template_name = 'housing.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Housing.objects.all()




    '''
    A method for it we want to post information for a listing that is not from the admin webiste
       - only included the street_address part of it here
    

    def post(request):
        street_address = request.POST.get('street address')
        #if not(street_address):
            #return HttpResponseRedirect(reverse('housing'))
        try:
            one_listing = Housing(street_address = street_address)
            one_listing.save()
        except(KeyError, Housing.DoesNotExist):
            return render(request, 'housing.html', {
              'error_message': "You didn't enter a listing."})
        return HttpResponseRedirect(reverse('housing:listing'))
'''