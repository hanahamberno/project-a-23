from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile, Property
from django.core.exceptions import ObjectDoesNotExist

#This code is modified from code that's part of this tutorial: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11&t=1143s

# (Hanah) want a user profile to be created for each new user
@receiver(post_save, sender=User) #signal = save
def create_user_profile(sender, instance, created, **kwargs):
    # (Seungeon) some user might not have user profile.
    # https://stackoverflow.com/questions/52244032/i-keep-getting-relatedobjectdoesnotexist-at-admin-login-how-do-i-successfully
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


# (Hanah) save profile function that saves profile everytime user object gets saved 
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# (Seungeon)
# Try this for creating/saving property
# @receiver(post_save, sender=Profile)
# def create_property(sender, instance, **kwargs):
#     try:
#         instance.property.save()
#     except ObjectDoesNotExist:
#         Property.objects.create(user=instance)
