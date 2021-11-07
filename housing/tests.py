from __future__ import unicode_literals

import datetime

from django.urls import reverse
from django.utils import timezone

from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Housing


class HousingModelTest(TestCase):
    def test_str_representation(self):
        house = Housing(title="Sample")
        self.assertEqual(str(house), house.title)

    def test_was_published_recently_with_old_listing(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_listing = Housing(listing_date=time)
        self.assertIs(old_listing.was_published_recently(), False)

    def test_was_published_recently_with_recent_listing(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_listing = Housing(listing_date=time)
        self.assertIs(recent_listing.was_published_recently(), True)

    def test_was_published_recently_with_future_listing(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_listing = Housing(listing_date=time)
        self.assertIs(future_listing.was_published_recently(), False)


class MainPageViewTest(TestCase):
    def test_mainPage(self):
        response = self.client.get('/housing/')
        self.assertEqual(response.status_code, 200)


class SearchResultsViewTest(TestCase):
    def test_resultsPage(self):
        response = self.client.get('/housing/search_results/')
        self.assertEqual(response.status_code, 200)

class ListingPageViewTest(TestCase):
    def test_listingPage(self):
        response = self.client.get('/housing/listing/')
        self.assertEqual(response.status_code, 200)

class ListingPageTest(TestCase):
    def test_incorrectimage(self):
        example_listing = Housing(title='Preston Apartments',
                                 image='https://img.offcampusimages.com/WgKq5tNLRIlQ_LylG-6iNPg4_U8=/660x440/left/top/smart/images/ecuyiiqoqaipb7j_op5cirqf4hphpcvvltyry0an_xu.jpeg')
        self.assertNotEqual(example_listing.image, 'https://img.offcampusimages.com/jWIDBfVflruISincDyFIjbhOMN4=/660x440/left/top/smart/images/mytnhdxke4fzlwt2qojoi5pprmokqbwia293dmuna2s.jpeg')

    def test_correctprice(self):
        another_example = Housing(title="Grandmarc at the Corner 4 Bedroom", price=900, street_address='301 15th St NW',
                                  city='Charlottesville', bedrooms=4, bathrooms=2)
        price_listing = another_example.price
        self.assertEqual(price_listing, 900)

# Create your tests here.
class GoogleLoginTests(OAuth2TestsMixin, TestCase):
    provider_id = GoogleProvider.id

    def get_mocked_response(self, last_name="Case", first_name="Test",
                            name="Test Case", email="testcase@test.com",
                            verified=True):
        return MockedResponse(200, """{"last_name": "%s", "first_name": "%s", "name": "%s", 
                                        "email": "%s", "id": "1",
                                        "verified": %s }
                                    """
                              % (
                                  last_name,
                                  first_name,
                                  name,
                                  email,
                                  (repr(verified).lower()),
                              )
                              )

    def test_Email_WrongUsername(self):
        first_name = "John"
        last_name = "Smith"
        email = "testcase@test.com"
        self.login(self.get_mocked_response(name=first_name + " " + last_name, email=email,
                                            first_name=first_name, last_name=last_name, verified=True))
        test_user = User.objects.get(email=email)
        self.assertEqual(test_user.username, "testcase")

    def test_Email_WrongEmail(self):
        first_name = "John"
        last_name = "Smith"
        email = "testcases@test.com"
        self.login(self.get_mocked_response(name=first_name + " " + last_name, email=email,
                                            first_name=first_name, last_name=last_name, verified=True))
        test_user = User.objects.get(email=email)
        self.assertNotEqual(test_user.username, "testcase")

# Citations

# Title: Program Talk - Python Examples
# Author: na
# Date: 10/18/2021
# Code version: na
# URL: https://programtalk.com/python-examples/allauth.tests.MockedResponse/
# Software License: na

# Title: Django Documentation
# Author: na
# Date: 10/18/2021
# Code version: na
# URL: https://docs.djangoproject.com/en/3.2/topics/testing/
# Software License: na

# Title: Django allauth Documentation
# Author: na
# Date: 10/18/2021
# Code version: na
# URL: https://django-allauth.readthedocs.io/en/latest/
# Software License: na

# Title: Mocking External API's in Python
# Author: na
# Date: 10/18/2021
# Code version: na
# URL: https://realpython.com/testing-third-party-apis-with-mocks/
# Software License: na

# Title: Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture
# Author: Corey Schafer
# Date: 08/31/2018
# Code version: na
# URL: https://www.youtube.com/watch?v=FdVuKt_iuSI&t=136s
# Software License: na
