from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EnrtyForm


# Create your views here.

def index(request):
  return render(request, 'playground/index.html')

@login_required
def topics(request):
  topics = Topic.objects.filter(owner=request.user).order_by('date_added')
  return render(request, 'playground/topics.html', {"topics":topics})


def topic_lim_user(topic, request):
  if topic.owner != request.user:
    raise Http404


@login_required
def topic(request, pk):
  topic = Topic.objects.get(id=pk)
  topic_lim_user(topic, request)
  entries = topic.entry_set.all().order_by('-date_added')
  return render(request, 'playground/topic.html', {'topic':topic, 'entries':entries})


@login_required
def new_topic(request):
  if request.method != 'POST': #no data submision, make a blank form
    form = TopicForm()
  else:
    form = TopicForm(request.POST) #post data submited, process dt
    if form.is_valid():
      new_topic = form.save(commit=False)
      new_topic.owner = request.user
      new_topic.save()
      # form.save()
      return redirect('playground:topics')
  return render(request, 'playground/new_topic.html', {'form':form})

@login_required
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
      return redirect('playground:topic', pk)
    else:
      print(form.errors)
  return render(request, 'playground/new_entry.html', {'topic':topic, 'form':form})
 
@login_required 
def edit_entry(request, pk):
  entry = Entry.objects.get(id=pk)
  topic = entry.topic
  topic_lim_user(topic, request)
  
  if request.method != 'POST':
    form = EnrtyForm(instance=entry) #prefill with current details
  else:
    form = EnrtyForm(instance=entry, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('topic', entry.topic.id)
  return render(request, 'playground/edit_entry.html', {'topic':topic, 'entry':entry, 'form':form})

def delete_entry(pk):
  entry = Entry.objects.get(id=pk)
  entry.delete()
  return render('playground/del_entry.html', {'entry':entry})