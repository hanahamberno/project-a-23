from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *

# Create your tests here.

class ProfileTest1(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            username = 'test_user',
            password = 'test_user',
            email = '12345@gmail.com'
        )

        test_profile = Profile.objects.get_or_create(user=test_user, image="default.jpg")
    
    # (Seungeon)
    # a test method to check if the __str__ method returns the correct username
    def test_profile_str(self):
        # (Seungeon) objects.get() should be unique
        # this method should be used only when you know this attritube is unique, such as id value
        # so .filter() returns the queryset, something like list, and we can index them.
        test_user = User.objects.filter(username='test_user')[0]
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        # (Seungeon) str() will call __str__() inside the Profile Model
        self.assertEqual(str(test_user), 'test_user')
        self.assertEqual(str(test_profile), f'{test_profile.user.username} Profile')


    # def testUserCanLogin(self):
    #     user = User.objects.get(username='test_user')
    #     profile = Profile.objects.get(user=user)
    #     print("helloooo")
    #     self.assertEqual(1,1)
