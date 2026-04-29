# from django.conf.urls import url
from django.urls import path
from . import views

#urlConf
urlpatterns = [
  # path('playground/hello', views.say_hello)
  
  # url(r'^$', views.index, name='index'), #homepage
  path('', views.index, name='home'),
  ]