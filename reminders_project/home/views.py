from django.shortcuts import render
from django.http import HttpResponse #, JsonResponse

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")

# def hello_json(request):
#     return JsonResponse ({"HI":"BRO"})

def index(request):
    return render (request,"home/index.html")
