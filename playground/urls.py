# from django.conf.urls import url
from django.urls import path
from . import views


#urlConf
urlpatterns = [
  path('', views.index, name='home'),
  path('topics/', views.topics, name='topics'),
  path('topic/<int:pk>/', views.topic, name='topic')
]