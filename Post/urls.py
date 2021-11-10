from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = "News"

urlpatterns = [
  path('', Home, name="Home"),
]
