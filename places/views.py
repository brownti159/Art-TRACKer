from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'places/home.html')

def map(request):
     return render(request, 'places/map.html')

# def home(request):
#     return render(request, 'places/home.html')
