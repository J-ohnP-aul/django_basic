from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_user(request):
  logout(request)
  return redirect('playground:home')

def register_v(request):
  if request.method != 'POST':
    form = UserCreationForm()
  else:
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      auth_user = authenticate(username=new_user.username,
                               password=request.POST['password1'])
      login(request, auth_user)
      return redirect('playground:home')
  return render(request, 'registration/register.html', {'form':form})