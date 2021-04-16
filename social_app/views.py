from django.shortcuts import render
from django.views.generic import ListView, DetailView
# (Seungeon)
from users.models import Profile
from django.db.models import Q
import requests 


def home(request):
    return render(request, 'social_app/home.html')

# (Seungeon)
# by default,
# url : <app>/<model>_<viewtype>.html
# in our case, 'users/profile_list.html'


# class ProfileListView(ListView):
#     # this behaves same as model = Profile.objects.get.all()
#     model = Profile
#     # The template_name attribute is used to tell Django to use a specific template name
#     # instead of the autogenerated default template name
#     template_name = 'social_app/home.html'
#     # Designates the name of the variable to use in the context.
#     # from Django official Docs
#     # https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-single-object/
#     context_object_name = 'profiles'
#     # ordering = [-some attribute] <- this will order it by whatever attribute in models.py specified

#     def get_queryset(self):
#         queryset = Profile.objects.exclude(user__username="admin")
#         return queryset

class ProfileListView(ListView):
    # this behaves same as model = Profile.objects.get.all()
    model = Profile
    # The template_name attribute is used to tell Django to use a specific template name
    # instead of the autogenerated default template name
    template_name = 'social_app/profile_list.html'
    # Designates the name of the variable to use in the context.
    # from Django official Docs
    # https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-single-object/
    context_object_name = 'profiles'
    # ordering = [-some attribute] <- this will order it by whatever attribute in models.py specified

    def get_queryset(self):
        # queryset = Profile.objects.filter(property__pk__isnull = True).exclude(user__username="admin").exclude(display_profile=False)
        queryset = Profile.objects.filter(Q(display_profile=True) & Q(property__display_property=False))
        return queryset

class PropertyListView(ListView):
    model = Profile
    template_name = 'social_app/property_list.html'
    context_object_name = "profiles"

    def get_queryset(self):
        queryset = Profile.objects.filter(Q(display_profile=True) & Q(property__display_property=True))
        return queryset

def profile_detail_view(request, pk):
    profile = Profile.objects.get(user__pk=pk)
    context = {
        "profile": profile,
        }
    return render(
        request=request,
        template_name='social_app/detail.html',
        context=context,
    )

# def profile_detail_view(request, pk):
    # profile = Profile.objects.get(user__pk=pk)
    # context = {
    #     "profile": profile,
    #     }
    # return render(
    #     request=request,
    #     template_name='social_app/detail.html',
    #     context=context,
    # )
    # pass


def about(request):
    return render(
        request=request,
        template_name='social_app/about.html'
    )

def twilio(request):
    return render(
        request=request,
        template_name='twilio/index.html'
    )
    #response = requests.get('https://api.groupme.com/v3/groups?token=INSERTTOKENHERE')
    #return render(request, 'social_app/groupme.html', {'response':response})
