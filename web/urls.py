
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name="home"),
  path('About.html', views.About, name="About"),
  
]
