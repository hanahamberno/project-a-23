from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *

# Create your tests here.

class ProfileTest1(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username = 'user1',
            password = 'user1',
            email = 'user1@user1.user1'
        )
        user1.save()

        profile1 = Profile.objects.create(user=user1, image="default.jpg")
        profile1.save()

    def testUserCanLogin(self):
        user = User.objects.get(username='user1')
        profile = Profile.objects.get(user=user)
        print("helloooo")
        self.AssertEqual(1,1)
