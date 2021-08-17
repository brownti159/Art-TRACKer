from django.shortcuts import render

def index(request):
    return render(request, 'places/home.html')

def map(request):
     return render(request, 'places/map.html')

def opening(request):
    return render(request, 'places/opening.html')

def hamburger(request):
    return render(request, 'places/hamburger.html')

