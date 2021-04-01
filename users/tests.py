from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *

# Create your tests here.


class ProfileModelTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            username='test_user',
            password='test_user',
            email='12345@gmail.com'
        )

        test_profile = Profile.objects.get_or_create(
            user=test_user,
            image="default.jpg"
        )

    # (Seungeon)
    # a test method to check if the __str__ method returns the correct username
    def test_profile_str(self):
        print("Testing __str__() method\n")
        # (Seungeon) objects.get() should be unique
        # this method should be used only when you know this attritube is unique, such as id value
        # so .filter() returns the queryset, something like list, and we can index them.
        test_user1 = User.objects.filter(username='test_user')[0]
        test_profile1 = Profile.objects.filter(user__username='test_user')[0]
        # (Seungeon) str() will call __str__() inside the Profile Model
        self.assertEqual(str(test_user1), 'test_user')
        self.assertEqual(str(test_profile1),
                         f'{test_profile1.user.username} Profile')

    # (Seungeon)
    # Django validation is mostly application level validation and not validation at DB level
    # Model validation is not run automatically on save/create of the model
    # If you want to validate your values at certain time in your code then you need to do it manually
    # ref: https://stackoverflow.com/questions/40881708/django-model-validator-not-working-on-create
    def test_profile_valid_graduation_year(self):
        test_profile1 = Profile.objects.filter(user__username='test_user')[0]
        test_profile1.graduation_year = 2022
        try:
            print("Tryint valid graduation year(2022)\n")
            test_profile1.full_clean()
            # Model.full_clean() validates the model fields, the field uniqueness
        except ValidationError:
            print("'test_profile_valid_graaduation_year'failed")
        else:
            test_profile1.save()

    # (Seungeon)
    # Try inserting invalid graduation_year into model
    # It should raise ValidationError
    def test_profile_invalid_graduation_year(self):
        test_profile1 = Profile.objects.filter(user__username='test_user')[0]
        test_profile1.graduation_year = 2040
        try:
            print("Tyring invalid graduation year(2040)\n")
            test_profile1.full_clean()
        except ValidationError:
            pass
        else:
            print("'test_profile_invalid_graduation_year'failed")
            test_profile1.save()

    # def testUserCanLogin(self):
    #     user = User.objects.get(username='test_user')
    #     profile = Profile.objects.get(user=user)
    #     print("helloooo")
    #     self.assertEqual(1,1)
