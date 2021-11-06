from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('listing/', views.ListingListView.as_view(), name='listing'),
    path('search_results/', views.search_results, name="search_results"),
    path('map/', views.housing_map, name="map")
]
