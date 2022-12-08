from django.shortcuts import render
from .models import Reminder
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    # Query the reminders table
    # - Return Json
    # - Return HTML
    reminders = Reminder.objects.all()
    # Exercise: return a dictionary with key called "reminders" and value reminders
    # list of dictionaries
    # { "reminders": [ 
    #    {"id": 1, "title": "blah blah", "description": "nice!"}, 
    #    {"id": 1, "title": "blah blah", "description": "nice!"}, 
    #    {"id": 1, "title": "blah blah", "description": "nice!"}]
    # }
    return JsonResponse({"reminders": list(reminders.values())})

# Cross-Site Request Forgery (CSRF)

@csrf_exempt
def new_reminder(request):
    # breakpoint()
    # parse json string
    data = json.loads(request.body)
    # titel = data.get("title")
    # description = data.get("description")
    # TODO: Store the reminder in the database and Return a dictionary object
    # as a JSON response
    r = Reminder.objects.create(title=data["title"], description=data["description"])
    return JsonResponse({"id": r.id, "title": r.title, "description": r.description})
    # return HttpResponse("Hello world")
