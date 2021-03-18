from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile

# (Hanah) want a user profile to be created for each new user
@receiver(post_save, sender=User) #signal = save
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# (Hanah) save profile function that saves profile everytime user object gets saved 
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profule.save()