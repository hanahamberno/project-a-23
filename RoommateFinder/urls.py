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
]


# (Seungeon) this is for the production. If debug is set to True, which means development mode,
# we can explicitly see the url for the profile picture on the browser.
# we don't want this to happen when it's being deployed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
