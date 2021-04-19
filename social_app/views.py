from django.shortcuts import render
from django.views.generic import ListView, DetailView
# (Seungeon)
from users.models import Profile, Property
from django.db.models import Q
import requests 


def home(request):
    profile = Profile.objects.all()
    context = {
        "profile": profile
    }
    return render(
        request=request, 
        template_name='social_app/home.html',
        context=context,
        )

# (Seungeon)l
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

class PreferenceListView(ListView):
    # this behaves same as model = Profile.objects.get.all()
    model = Profile
    # The template_name attribute is used to tell Django to use a specific template name
    # instead of the autogenerated default template name
    template_name = 'social_app/top_matches_list.html'
    # Designates the name of the variable to use in the context.
    # from Django official Docs
    # https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-single-object/
    context_object_name = 'profiles'
    # ordering = [-some attribute] <- this will order it by whatever attribute in models.py specified

    def get_queryset(self):
        # profile = property_list if user wants to be matched w/ ppl w/ properties, profile_list if user wants to be match w/ onyl no propt, both if no preference
        # score = 0
        # top_profile_list = []
        # for all profile in profiles:
            # for all preferences:
                # if preference matches listing info:
                    # score += 1
                    # top_profile_list.append((profile, score))
        # sort(top_profile_list)
        # display top_profile_list[:10]
                    
        # get "scores", where score = # of matches btwn preferences + given profile
        # sort scores from greatest to least
        # diplay top 10 profiles that have the highest score (first 10 profiles in sorted scores list)

        score = 0
        top_profile_list = list()
        # queryset = Profile.objects.filter(property__pk__isnull = True).exclude(user__username="admin").exclude(display_profile=False)
        queryset = Profile.objects.filter(Q(display_profile=True) & Q(property__display_property=False))
        return queryset

# Kathy: helper method to calculate score for matching algorithm
# d = the other user to compare to
# profile = the current user
# match_type = the type of users (d) that the current user (profile) wants to match with
#               **this is either "profile" or "property"
#               "profile": match with users who don't have a property
#               "property": match with users who have a property
def calculate_score(d, profile, match_type):
    print("calculate_score in")
    score = 0
    # score w/ others who don't have a property
    if(match_type == "profile"):
        for pref in d.preference_list(): 
            print(pref)
            if pref != None:
                # check if the person has a property or not and assign variables accordingly
                comp_val = 0
                if(hasattr(d, "Property")):
                    if(d.property.display_property):
                        comp_val = profile.property.rent
                else:
                    comp_val = profile.max_price
                
                # score things
                if(pref == "max_price" and d.max_price >= comp_val):
                    score += 1
                if(pref == "on_grounds" and d.on_grounds == profile.on_grounds):
                    score += 1
                if(pref == "pref_gender"):
                    if(profile.pref_gender == "NO_PREFERENCE"):
                        score += 1
                    else:
                        if(d.gender == profile.pref_gender):
                            score += 1
    # score w/ others who have a property
    elif(match_type == "property"):
        for pref in d.preference_list():
            print(pref)
            if pref != None:
                # score things
                if(pref == "max_price" and d.property.rent <= profile.max_price):
                    print("rent is good")
                    score += 1
                if(pref == "on_grounds" and d.property.on_grounds == profile.on_grounds):
                    print("on grounds is good")
                    score += 1
                if(pref == "pref_gender"):
                    if(profile.pref_gender == "NO_PREFERENCE"):
                        print("gender is good")
                        score += 1
                    else:
                        if(d.gender == profile.pref_gender):
                            print("gender is good")
                            score += 1
    return score

def preference_list_view(request):
    profile_all = Profile.objects.all()
    profile = Profile.objects.get(user__pk=request.user.pk)
    top_profile_list = []

    if (profile.match_list == "Both" or not profile.match_list):
        display_list = Profile.objects.filter(Q(display_profile=True)).exclude(user__pk=request.user.pk)
        print(display_list)
        score = 0
        for d in display_list:
            # if d created a 
            print(str(d) + " hasattr: " + str(hasattr(d, 'property')))
            if(hasattr(d, 'property')): #either False or True
                # and d wants to display the property
                print("display prop: " + str(d.property.display_property))
                if (d.property.display_property):
                    print(d, "display_property in")
                    score = calculate_score(d, profile, "property")
                else:
                    print(d, "display_profile in")
                    score = calculate_score(d, profile, "profile")
            else:
                print(d, "display_profile in")
                score = calculate_score(d, profile, "profile")
            top_profile_list.append((score, d))

        # if d is a person w/ no property: score = calculate_score(d, profile, "profile")
        # else if d is a person w/ a property: score = calculate_score(d, profile, "property")


    elif (profile.match_list == "Profile"):
        display_list = Profile.objects.filter(Q(display_profile=True) & Q(property__display_property=False)).exclude(user__pk=request.user.pk)
        score = 0
        for d in display_list:
            score = calculate_score(d, profile, "profile")
            top_profile_list.append((score, d))

    elif (profile.match_list == "Property"):
        display_list = Profile.objects.filter(Q(display_profile=True) & Q(property__display_property=True)).exclude(user__pk=request.user.pk)
        print(display_list)
        score = 0
        for d in display_list:
            score = calculate_score(d, profile, "property")
            top_profile_list.append((score, d))
    
    top_profile_list = sorted(top_profile_list, key=lambda x: x[0], reverse=True)
    print(top_profile_list[0:15])
    context = {
        "display_list": top_profile_list[0:15]
    }
    return render(
        request=request,
        template_name='social_app/top_matches_list.html',
        context=context,
    )
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
