# This file, urls.py, defines the URL patterns for the myfirstapp Django application.
# It specifies how incoming HTTP requests should be mapped to view functions within the application.
# In this file:
# - The urlpatterns list contains a single path() function call that maps the root URL ('') to the 'myfirstapp' view function
#   from the views module of the myfirstapp application.
# - The name argument 'myfirstapp' provides a unique identifier for this URL pattern, which can be used to reverse
#   the URL in templates or views.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfirstapp, name='myfirstapp'),
]


