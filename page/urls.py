# Add the url for the app
from django.urls import path
from page.views import hello_world

urlpatterns = [
  path('hello-world/', hello_world),
]