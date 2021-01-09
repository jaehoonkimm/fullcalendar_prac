from django.shortcuts import render
from .models import CalendarEvent

# Create your views here.

def home(request):
    # define Calendar QuerySet
    events = CalendarEvent.objects.all()

    return render(request, 'index.html', {'events': events})