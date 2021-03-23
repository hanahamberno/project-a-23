from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
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

    def __str__(self):
        return f'{self.user.username} Profile' 

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)

    #     # resize image if necessary
    #     if (img.height > 300 or img.width > 300):
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

