from django.shortcuts import render, redirect#Ben
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, PropertyUpdateForm

#(Seungeon)
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # prop_form = PropertyUpdateForm(request.POST,
        #                                request.FILES,
        #                                instance = request.property #fix this
        #                                )
        if u_form.is_valid() and p_form.is_valid(): #and prop_form.is_valid():
            u_form.save()
            p_form.save()
            #prop_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #prop_form = PropertyUpdateForm(instance = request.property) #fix this

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'prop_form' : prop_form
    }

    return render(request, 'users/profile.html', context) 