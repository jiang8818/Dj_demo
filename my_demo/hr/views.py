from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hr_index(request):
    return render(request, 'hr_index.html')
