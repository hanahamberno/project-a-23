from django.shortcuts import render

def home(request):
    return render(request, 'social_app/index.html')