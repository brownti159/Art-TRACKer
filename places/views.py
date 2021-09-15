from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from places.models import Artist, Work
from places.serializers import ArtistSerializer, WorkSerializer
from django.shortcuts import render, get_object_or_404
from .models import Work


def index(request):
    return render(request, 'places/home.html')

def map(request):
    return render(request, 'places/map.html')

def about(request):
    return render(request, 'places/about.html')

def tutorial(request):
    return render(request, 'places/tutorial.html')

def contact(request):
    return render(request, 'places/contact.html')
    
def hamburger(request):
    return render(request, 'places/hamburger.html')
    

@csrf_exempt
def artist_list(request):
    # List all artists, or create a new one.
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def artist_detail(request, pk):
    # retrieve, update, or delete an artist
    try: 
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(artist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        artist.delete()
        return HttpResponse(status=204)


@csrf_exempt
def work_list(request):
    # List all artworks, or create a new one.
    if request.method == 'GET':
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = WorkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def work_detail(request, pk):
    # retrieve, update, or delete an artwork
    try: 
        work = Work.objects.get(pk=pk)
    except Work.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WorkSerializer(work)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WorkSerializer(work, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        work.delete()
        return HttpResponse(status=204)

def details(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'places/details.html',{"work":work} )
