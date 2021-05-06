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
                test_profile = Profile.objects.create(
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
        print("Testing profile __str__() method...")
        test_user = User.objects.filter(username='test_user')[0]
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        self.assertEqual(str(test_user), 'test_user')
        self.assertEqual(str(test_profile), f'{test_profile.user.username} Profile')
    
    def test_profile_valid_graduation_year(self):
        print("Testing profile valid graduation year...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.graduation_year = 2022
        self.assertTrue(test_profile.is_valid_graduation_year())

    def test_profile_invalid_graduation_year(self):
        print("Testing profile invalid graduation year...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.graduation_year = 2040
        self.assertFalse(test_profile.is_valid_graduation_year())
    
    def test_profile_valid_age(self):
        print("Testing profile valid age...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.age = 19
        self.assertTrue(test_profile.is_valid_age())
    
    def test_profile_invalid_age(self):
        print("Testing profile invalid age...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.age = 2040
        self.assertFalse(test_profile.is_valid_age())
    
    def test_profile_valid_phone_number(self):
        print("Testing profile valid phone number...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.phone_number="472-555-0291"
        self.assertTrue(test_profile.is_valid_phone_number())
    
    def test_profile_invalid_phone_number(self):
        print("Testing profile invalid phone number...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.phone_number="472-555-02914"
        self.assertFalse(test_profile.is_valid_phone_number())
    
    def test_profile_valid_max_price(self):
        print("Testing profile valid max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = 1500
        self.assertTrue(test_profile.is_valid_max_price())
    
    def test_profile_invalid_max_price(self):
        print("Testing profile invalid max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = -500
        self.assertFalse(test_profile.is_valid_max_price())
    
    # 0 should be a valid price
    def test_profile_edge_case_max_price(self):
        print("Testing profile edge case max price...")
        test_profile = Profile.objects.filter(user__username='test_user')[0]
        test_profile.max_price = 0
        self.assertTrue(test_profile.is_valid_max_price())



# Tests for the Property Model
class PropertyModelTest(TestCase):
    def setUp(self):
        try:
            with transaction.atomic():
                test_user = User.objects.create_user(
                    first_name='hello',
                    last_name='hi',
                    username='test_user',
                    password='test_user',
                    email='123456@gmail.com'
                )

                test_user.full_clean()
                test_user.save()
        except:
            test_user = User.objects.filter(username='test_user')[0]

        try:
            with transaction.atomic():
                test_profile = Profile.objects.create(
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
            test_profile = Profile.objects.filter(user=test_user)[0]
        
        try:
            with transaction.atomic():
                test_property = Property.objects.create(
                    profile=test_profile,
                    image='default_property.jpg'
                )

                test_property.full_clean()
                test_property.save()
        except:
            pass

    def test_property_str(self):
        print("Testing property __str__() method...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        self.assertEqual(str(test_property), f'{test_property.profile.user.first_name} {test_property.profile.user.last_name}\'s Property')


    def test_property_valid_rent(self):
        print("Testing property valid rent...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.rent = 1500
        self.assertTrue(test_property.is_valid_rent())

    def test_property_invalid_rent(self):
        print("Testing property invalid rent...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.rent = -200
        self.assertFalse(test_property.is_valid_rent())

    # 0 is a valid rent number
    def test_property_edge_case_rent(self):
        print("Testing property edge case rent...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.rent = 0
        self.assertTrue(test_property.is_valid_rent())
    
    def test_property_valid_num_roommates(self):
        print("Testing property valid num roommates...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.current_number_of_roommates = 2
        self.assertTrue(test_property.is_valid_num_roommates())

    def test_property_invalid_num_roommates(self):
        print("Testing property invalid num roommates...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.current_number_of_roommates = 34
        self.assertFalse(test_property.is_valid_num_roommates())
    
    # 0 is a valid current number of roommates
    def test_property_edge_case_num_roommates(self):
        print("Testing property edge case num roommates...")
        test_property = Property.objects.filter(profile__user__username='test_user')[0]
        test_property.current_number_of_roommates = 0
        self.assertTrue(test_property.is_valid_rent())
