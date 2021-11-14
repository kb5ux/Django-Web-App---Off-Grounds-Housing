from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('listings/', views.ListingListView.as_view(), name='listing'),
    path('listings/details/<int:id>/', views.ListingDetails, name='listing_details'),
    path('search_results/', views.search_results, name="search_results"),
    path('map/', views.housing_map, name="map"),
    path('addreview/<int:id>/', views.add_review, name="add_review")

]
