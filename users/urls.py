from django.conf import urls
from django.contrib.auth import login
from django.urls import path

from . import views
app_name = "users"

urlpatterns = [
  path('logout', views.logout_user, name='logout')
  #path('login/', login,{'template_name':'users/login.html'}, name='users:login'),
]
