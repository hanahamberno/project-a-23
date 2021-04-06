# Ben
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Property


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
            'image',
            'age',
            'bio',
            'pronouns', 
            'graduation_year',
            'phone_number', 
            'on_grounds', 
            'max_price'
        ]
class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'rent',
            'amenities',
            'address',
            'furnished', 
            'current_number_of_roommates', 
            'number_of_roommates_seeking', 
            'room_type',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'building_policies',
            'lease_duration',
            'building_type',
            'other_details']