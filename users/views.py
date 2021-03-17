from django.shortcuts import render


#(Seungeon)
def profile(request):
    return render(request=request, template_name='users/profile.html')
