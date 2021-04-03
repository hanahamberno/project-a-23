from django.contrib import admin
# import our users model
from . import models
from django.contrib.auth.models import User

# (Seungeon) same as 'admin.site.register(Profile),it has more decorative features.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'age',
    )

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

# (Seungeon)
# Property panel on admin site
@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    # (Seungeon)
    # if this is not setup, admin will have "propertys"
    verbose_name_plural = "properties"
    pass
