from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")

# def hello_json(request):
#     return JsonResponse ({"HI":"BRO"})


def index(request):

    # create a range of numbers (0 to 2000)
    numbers = range(0, 2000)

    # template context "variables"
    context = {"numbers": numbers}

    return render(request, "home/index.html", context)

# def index(request):
#     return render (request,"home/index.html")

def hello_json(request):
   return JsonResponse ({"HI":"BRO"})
