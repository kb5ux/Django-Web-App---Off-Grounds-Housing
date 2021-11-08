from django.contrib import admin
from django.db import models
import datetime

# Create your models here.
from django.utils import timezone


class Housing(models.Model):
    title = models.CharField(max_length=200)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    zipcode = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)  # Can have 1.5 baths
    square_feet = models.IntegerField()
    is_available = models.BooleanField(default=True)
    listing_date = models.DateTimeField(default=timezone.now, blank=True)
    #image = models.ImageField(null=True, blank=True, upload_to='images/')

    @admin.display(
        boolean=True,
        ordering='listing_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.listing_date <= now

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    review_description = models.TextField(blank=True)
    review_score = models.DecimalField(max_digits=2, decimal_places=1)
    review_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

class RentalCompany(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
