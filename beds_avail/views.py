from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    hospitals = Hospital.objects.all()
    # return HttpResponse('This is the home page for beds_avail section.')
    return render(request, 'beds_avail_home.html', {'hospitals':hospitals})


