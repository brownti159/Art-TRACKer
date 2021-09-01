from django.shortcuts import render, get_object_or_404
from .models import Work


def index(request):
    return render(request, 'places/home.html')


def map(request):
    return render(request, 'places/map.html')


def hamburger(request):
    return render(request, 'places/hamburger.html')


def details(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'places/details.html',{"work":work} )
