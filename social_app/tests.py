# Django built-ins.
from django.test import TestCase
from django.contrib.auth.models import User
# Models
from users.models import Profile
# Create your tests here.

# (Seungeon)
# test if the homepage is loaded properly
class SocialAppHomeTests(TestCase):
    def test_home(self):
        # get the response of HTTP GET method on the url '/'
        response = self.client.get('/')
        # if the response.status_code is 200, test passes.
        self.assertEqual(response.status_code, 200)
