# Ben
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Property

#This code is modified from code that's part of this tutorial: https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12&t=4s



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'display_profile',
            'image',
            'age',
            'bio',
            'graduation_year',
            'gender',
            'pronouns',
            'phone_number',
        ]

class PreferenceUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'match_list',
            'on_grounds',
            'max_price',
            'pref_gender',
        ]


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'display_property',
            'image',
            'rent',
            'amenities',
            'address',
            'on_grounds',
            'furnished',
            'current_number_of_roommates',
            'number_of_roommates_seeking',
            'room_type',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'building_policies',
            'lease_duration',
            'building_type',
            'other_details',
        ]
