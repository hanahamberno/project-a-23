"""RoommateFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.contrib.auth import views as auth_views (Hanah) idk if we need this, it was already there from the tutorial
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from model
from users import views as user_views

urlpatterns = [
    path('', include("social_app.urls", namespace="social_app")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #(Seungeon) for the profile url
    path('profile/', user_views.profile, name='profile'),
    path('property/', user_views.property_update, name='property'),
    path(r'', include('chatapp.urls')),
    path('inbox', include('messages.urls', namespace="messages")),
]


if settings.DEBUG: # (Hanah) if in debug mode, then we want to add following to url patterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # (Hanah) Serving files uploaded by a user during development