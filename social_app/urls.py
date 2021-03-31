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
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileListView

app_name = 'social_app'

urlpatterns = [
    path('', ProfileListView.as_view(), name='home'),
    # path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>', views.profile_detail_view, name='profile_detail_view'),
    #path('', views.home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(template_name='social_app/home.html'), name='logout'),
    path('about', views.about, name="about"),
]
