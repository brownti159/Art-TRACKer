from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from places.models import Work
from places.serializers import WorkSerializer

def index(request):
    return render(request, 'places/home.html')

def map(request):
     return render(request, 'places/map.html')

def hamburger(request):
    return render(request, 'places/hamburger.html')


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