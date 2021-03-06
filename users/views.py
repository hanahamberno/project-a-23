from django.shortcuts import render, redirect # Ben
from django.contrib import messages
from .forms import *
from .models import Property

# makes users login before they can see a page -- Kathy
from django.contrib.auth.decorators import login_required

#(Seungeon)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST,
            instance = request.user
        )

        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance = request.user.profile
        )

        pref_form = PreferenceUpdateForm(
            request.POST,
            request.FILES,
            instance = request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid() and pref_form.is_valid():
            u_form.save()
            p_form.save()
            pref_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('social_app:home')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        pref_form = PreferenceUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pref_form': pref_form,
    }

    return render(request, 'users/profile.html', context)


def property_update(request):
    if request.method == 'POST':
        prop_form = PropertyUpdateForm(
            request.POST,
            request.FILES,
            instance = request.user.profile.property
        )

        if prop_form.is_valid():
            prop_form.save()
            messages.success(request, 'Your property has been updated!')
            return redirect('social_app:property_list')

    else:
        # (Seungeon)
        # property model shoudl be created first which shoudl point to
        # the correct 'profile' model.
        prop = Property.objects.get_or_create(profile = request.user.profile)
        prop_form = PropertyUpdateForm(instance = request.user.profile.property)

    context = {
        'prop_form': prop_form,
    }

    return render(
        request = request,
        template_name = 'users/property_form.html',
        context = context,
    )
