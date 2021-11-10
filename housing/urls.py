from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('listing/', views.ListingListView.as_view(), name='listing'),
    path('search_results/', views.search_results, name="search_results"),
    path('reviews/list/', views.ReviewsListView.as_view(), name='reviews_list'),
    path('map/', views.housing_map, name="map"),
    path('reviews/', views.SubmitReviewView.as_view(), name='review'),
    path('reviews/submit/', views.post, name='submit')

]
