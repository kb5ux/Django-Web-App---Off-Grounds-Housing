from django.contrib import admin
from .models import Housing

'''


class HousingAdmin(admin.ModelAdmin):
   fields = ('title','street_address','city','state','zipcode','description','price','bedrooms','bathrooms',
                    'square_feet','is_available','listing_date')

'''
# Register your models here.

admin.site.register(Housing)
