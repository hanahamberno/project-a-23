from django.contrib import admin
#import our users model
from . import models

# (Seungeon) same as 'admin.site.register(Profile),it has more decorative features.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass