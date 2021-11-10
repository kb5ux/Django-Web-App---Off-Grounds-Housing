from django.contrib import admin
from .models import Housing, Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['review_title']}),
        (None,               {'fields': ['review_description']}),
        (None,               {'fields': ['listing_id']}),
    ]
    list_display = ('review_title','review_description')


admin.site.register(Housing)
admin.site.register(Review, ReviewAdmin)
