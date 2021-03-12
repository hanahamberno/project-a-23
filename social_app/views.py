from django.shortcuts import render

def home(request):
    return render(request, 'social_app/home.html')


def about(request):
    return render(
        request=request, 
        template_name='social_app/about.html'
    )