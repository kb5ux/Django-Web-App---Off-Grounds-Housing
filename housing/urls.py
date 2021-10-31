from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/', views.ListingListView.as_view(), name = 'listing')
]