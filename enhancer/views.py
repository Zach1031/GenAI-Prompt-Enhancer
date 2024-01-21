from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def index(request):
    print('here')
    return render(request, "sea.html")

# Create your views here.
