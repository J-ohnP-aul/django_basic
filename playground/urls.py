# from django.conf.urls import url
from django.urls import path
# from django.urls. import url
from . import views


#urlConf
app_name = 'playground'

urlpatterns = [
  path('', views.index, name='home'),
  path('topics/', views.topics, name='topics'),
  path('topic/<int:pk>/', views.topic, name='topic'),
  path('new_topic', views.new_topic, name='new_topic'),
  path('new_entry/<int:pk>/', views.new_entry, name='new_entry'),
  path('edit_entry/<int:pk>/', views.edit_entry, name='edit_entry'),
  path('del_entry/<int:pk>/', views.delete_entry, name='del_entry')  #to delete entry
]