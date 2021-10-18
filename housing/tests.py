from __future__ import absolute_import, unicode_literals
from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse
from django.contrib.auth.models import User
from django.test import TestCase


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
