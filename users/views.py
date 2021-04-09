from django.shortcuts import render, redirect#Ben
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, PropertyUpdateForm
from .models import Property
# makes users login before they can see a page, Kathy
from django.contrib.auth.decorators import login_required

#(Seungeon)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        #endif
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    #endif

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context) 

def property_update(request):
    if request.method == 'POST':
        prop_form = PropertyUpdateForm(request.POST,
                                       request.FILES,
                                       instance = request.user.profile.property #fix this
                                       )
        if prop_form.is_valid(): #and prop_form.is_valid():
            prop_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        #endif

    else:
        # (Seungeon)
        # property model shoudl be created first which shoudl point to
        # the correct 'profile' model.
        prop = Property.objects.get_or_create(profile=request.user.profile)
        prop_form = PropertyUpdateForm(instance=request.user.profile.property) #fix this
    #endif

    context = {
        'prop_form' : prop_form,
    }
    return render(
        request=request,
        template_name='users/property_update.html',
        context=context,
    )