from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from .models import Topic, Entry
from .forms import TopicForm, EnrtyForm


# Create your views here.

def index(request):
  return render(request, 'playground/index.html')

def topics(request):
  topics = Topic.objects.order_by('date_added')
  return render(request, 'playground/topics.html', {"topics":topics})

def topic(request, pk):
  topic = Topic.objects.get(id=pk)
  entries = topic.entry_set.order_by('-date_added')
  return render(request, 'playground/topic.html', {'topic':topic, 'entries':entries})

def new_topic(request):
  if request.method != 'POST': #no data submision, make a blank form
    form = TopicForm()
  else:
    form = TopicForm(request.POST) #post data submited, process dt
    if form.is_valid():
      form.save()
      return redirect('topics')
  return render(request, 'playground/new_topic.html', {'form':form})

def new_entry(request, pk):
  topic = Topic.objects.get(id=pk)
  if request.method != 'POST':
    form = EnrtyForm()
  else:
    form = EnrtyForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)      
      new_entry.topic = topic
      new_entry.save()
      return redirect('topic', pk)
  return render(request, 'playground/new_entry.html', {'topic':topic, 'form':form})
  
def edit_entry(request, pk):
  entry = Entry.objects.get(id=pk)
  topic = entry.topic
  
  if request.method != 'POST':
    form = EnrtyForm(instance=entry) #prefill with current details
  else:
    form = EnrtyForm(instance=entry, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('topic', pk)
  return render(request, 'playground/edit_entry.html', {'topic':topic, 'entry':entry, 'form':form})

    