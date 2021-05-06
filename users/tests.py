from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *
from django.db import transaction


# Tests for the Profile Model
class ProfileModelTest(TestCase):
    def setUp(self):
        try:
            with transaction.atomic():
                test_user = User.objects.create_user(
                    username='test_user',
                    password='test_user',
                    email='123456@gmail.com'
                )
        except:
            test_user = User.objects.filter(username='test_user')[0]

        try:
            with transaction.atomic():
                Profile.objects.create(
                    user=test_user,
                    image="default.jpg",
                    bio="hello",
                    pronouns="she/they",
                    on_grounds=Profile.ON_GROUNDS,
                    display_profile=True
                )
                test_profile.full_clean()
                test_profile.save()
        except:
            pass

    def test_profile_str(self):
        print("Testing __str__() method...")
        test_user = User.objects.filter(username='test_user')[0]
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        self.assertEqual(str(test_user), 'test_user')
        self.assertEqual(str(test_profile), f'{test_profile.user.username} Profile')
    
    def test_profile_valid_graduation_year(self):
        print("Testing valid graduation year...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.graduation_year = 2022
        self.assertTrue(test_profile.is_valid_graduation_year())

    def test_profile_invalid_graduation_year(self):
        print("Testing invalid graduation year...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.graduation_year = 2040
        self.assertFalse(test_profile.is_valid_graduation_year())
    
    def test_profile_valid_age(self):
        print("Testing valid age...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.age = 19
        self.assertTrue(test_profile.is_valid_age())
    
    def test_profile_invalid_age(self):
        print("Testing invalid age...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.age = 2040
        self.assertFalse(test_profile.is_valid_age())
    
    def test_profile_valid_phone_number(self):
        print("Testing valid phone number...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.phone_number="472-555-0291"
        self.assertTrue(test_profile.is_valid_phone_number())
    
    def test_profile_invalid_phone_number(self):
        print("Testing invalid phone number...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.phone_number="472-555-02914"
        self.assertFalse(test_profile.is_valid_phone_number())
    
    def test_profile_valid_max_price(self):
        print("Testing valid max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = 1500
        self.assertTrue(test_profile.is_valid_max_price())
    
    def test_profile_invalid_max_price(self):
        print("Testing invalid max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = -500
        self.assertFalse(test_profile.is_valid_max_price())
    
    # 0 should be a valid price
    def test_profile_edge_case_max_price(self):
        print("Testing edge case max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = 0
        self.assertTrue(test_profile.is_valid_max_price())
