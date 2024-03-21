from django.shortcuts import render

def mysecondapp(request):
    return render(request, 'second_welcome.html')
