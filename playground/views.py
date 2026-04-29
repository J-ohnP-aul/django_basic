from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Topic, Entry

# Create your views here.

def index(request):
  return render(request, 'playground/index.html')

def topics(request):
  topics = Topic.objects.order_by('date_added')
  return render(request, 'playground/topics.html', {"topics":topics})

def topic(request, pk):
  topic = Topic.objects.get(id=pk)
  entry = topic.entry_set.order_by('-date_added')
  return render(request, 'playground/topic.html', {'topic':topic, 'entry':entry})
