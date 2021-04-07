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
        #'prop_form' : prop_form
    }

    return render(request, 'users/profile.html', context) 

def property_update(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   #it is profile.property because it's OneToOne field
                                   instance=request.user.profile)
        prop_form = PropertyUpdateForm(request.POST,
                                       request.FILES,
                                       instance = request.user.profile.property #fix this
                                       )
        if u_form.is_valid() and p_form.is_valid() and prop_form.is_valid(): #and prop_form.is_valid():
            u_form.save()
            p_form.save()
            prop_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #we need to make some sort of new property object before running this next line
        prop_form = PropertyUpdateForm(instance = request.user.profile.property) #fix this

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'prop_form' : prop_form
    }
    return render(
        request=request,
        template_name='users/property_update.html',
        context=context,
    )