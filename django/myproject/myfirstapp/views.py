# This file contains the view functions for the myfirstapp Django application.
# Views are responsible for processing user requests, interacting with models or other data sources,
# and returning an appropriate HTTP response. Each view function corresponds to a specific URL route.
# In this file:
# - The 'myfirstapp' function takes a request object and renders the 'first_welcome.html' template using the render shortcut.
# - This function is responsible for handling requests related to the 'myfirstapp' URL route.

from django.shortcuts import render

def myfirstapp(request):
    return render(request, 'first_welcome.html')


