from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Event


def index(request):
    latest_events_list = Event.objects.order_by('-creation_time')[:5]
    context = {
        'latest_events_list': latest_events_list
    }
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/detail.html", {'event': event})
