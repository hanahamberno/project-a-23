from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
#from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from PIL import Image

# (Seungeon)
# This is used for amenities.
# We have to have each amenity 'object'
# So whenever we create a amenity, this will be created
class AbstractItem(models.Model):
    name = models.CharField(max_length=30)
    
    # (Seungeon)
    # abstract = True will prevent this class from storing
    # in the DB.
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Profile(models.Model):

    ON_GROUNDS = "on-grounds"
    OFF_GROUNDS = "off-grounds"
    NO_PREFERENCE = "no preference"

    GROUNDS_CHOICES = (
        (ON_GROUNDS, "On-Grounds"),
        (OFF_GROUNDS, "Off-Grounds"),
        (NO_PREFERENCE, "No Preference"),
    )

    user = models.OneToOneField(
        User,
        null=True,
        # (Seungeon)models.CASCADE => if the 'User' is deleted, profile is also deleted.
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        # (Seungeon)if the user doesn't specify the image, this image will be the default image
        default='default.jpg',
        # (Seungeon)the dir that the image will be uploaded to when the user uploads profile pic
        # it will create a dir called "profile_pics"
        upload_to="profile_pics",
    )
    age = models.IntegerField(
        blank=True,
        validators=[MinValueValidator(0),MaxValueValidator(150)],
        null=True,
    )

    bio = models.TextField(blank=True, default='')

    graduation_year = models.IntegerField(
        blank=True,
        default=2021,
        validators=[MinValueValidator(2021), MaxValueValidator(2025)],
        null=True,
    )

    pronouns = models.CharField(blank=True, max_length=50,)

    phone_number = PhoneField(blank=True, max_length=14,)

    on_grounds = models.CharField(
        blank=True,
        choices=GROUNDS_CHOICES,
        max_length=50
    )

    max_price = models.IntegerField(
        blank=True,
        validators=[MinValueValidator(0),MaxValueValidator(10000)],
        default=600,
    )

    display_profile = models.BooleanField(
        blank=True,
        default=False,
    )
    # attributes needed:
    # 2. graduation year -> Char(with number)? Integer?
    # 3. Age -> Integer
    # 4. Pronouns(she/he) -> Char
    # 5. Bio -> textField
    # 6. Phone Number -> Char? is there anything specifically for PhoneNumber
    # 7. On-Grounds/Off-Grounds -> char
    # 8. Max_Price -> Integer

    def __str__(self):
        return f'{self.user.username} Profile'

    def is_valid_graduation_year(self):
        if self.graduation_year != None:
            if self.graduation_year < 2021 and self.graduation_year > 2025:
                raise ValidationError("Invalid year")
        return True

    # def save(self):
    #    super().save()
    #    img = Image.open(self.image.path)

        # resize image if necessary
    #    if (img.height > 300 or img.width > 300):
    #        output_size = (300, 300)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)

    #     # resize image if necessary
    #     if (img.height > 300 or img.width > 300):
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

# (Seungeon)
# Amenity class which inherited from AbstractItem
# AbstractItem will add each amenity
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Amenities" 
    def __str__(self):
        return self.name

class Property(models.Model):
    class Meta:
        verbose_name_plural = "Properties"

    FURNISHED = "Furnished"
    UNFURNISHED = "Unfurnished"
    FURNISHED_CHOICES = (
        (FURNISHED, "Furnished"),
        (UNFURNISHED, "Unfurnished"),
    )

    SINGLE = "Single"
    DOUBLE = "Double"
    EITHER = "Either"

    SINGLE_DOUBLE_CHOICES = (
        (SINGLE, "Single Room"),
        (DOUBLE, "Double Room"),
        (EITHER, "Either Single or Double"),
    )

    APARTMENT = "Apartment"
    HOUSE = "House"
    TOWNHOUSE = "Townhouse"
    OTHER = "Other"

    BUILDING_TYPE_CHOICES = (
        (APARTMENT, "Apartment"),
        (HOUSE, "House"),
        (TOWNHOUSE, "Townhouse"),
        (OTHER, "Other"),
    )

    profile = models.OneToOneField(
        Profile,
        null=True,
        # (Seungeon)models.CASCADE => if the 'Profile' is deleted, properties is also deleted.
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        # (Seungeon)if the user doesn't specify the image, this image will be the default image
        default='default_property.jpg',
        # (Seungeon)the dir that the image will be uploaded to when the user uploads profile pic
        # it will create a dir called "profile_pics"
        upload_to="property_pics",
    )

    rent = models.IntegerField(
        blank=True, 
        validators=[MinValueValidator(0),MaxValueValidator(10000)], 
        null=True,
    )

    amenities = models.TextField(blank = True, default='')

    address = models.CharField(
        verbose_name="Address/Location",
        blank = True, 
        max_length = 200
    )

    furnished = models.CharField(
        blank = True,
        choices = FURNISHED_CHOICES,
        max_length = 50,
    )

    current_number_of_roommates = models.IntegerField(
        blank = True,
        validators=[MinValueValidator(1),MaxValueValidator(20)], 
        null=True,
    )

    number_of_roommates_seeking = models.IntegerField(
        blank = True,
        validators=[MinValueValidator(1),MaxValueValidator(20)], 
        null=True,
    )

    room_type = models.CharField(
        blank = True,
        choices = SINGLE_DOUBLE_CHOICES,
        max_length = 50,
    )

    number_of_bedrooms =  models.IntegerField(
        blank = True,
        validators=[MinValueValidator(1),MaxValueValidator(20)], 
        null=True,
    )

    number_of_bathrooms =  models.IntegerField(
        blank = True,
        validators=[MinValueValidator(1),MaxValueValidator(20)], 
        null=True,
    )

    building_policies = models.TextField(blank=True, default='')

    lease_duration = models.IntegerField(
        'Lease Duration (Months)',
        blank = True,
        validators=[MinValueValidator(1),MaxValueValidator(72)], 
        null=True,
        default = 12,
    )

    building_type =  models.CharField(
        blank = True,
        choices = BUILDING_TYPE_CHOICES,
        max_length = 50,
    )

    other_details = models.TextField(blank=True, default='')

    display_property = models.BooleanField(
        blank=True,
        default=False,
    )

    def __str__(self):
       return f"{self.profile.user.first_name} {self.profile.user.last_name}'s Property"
