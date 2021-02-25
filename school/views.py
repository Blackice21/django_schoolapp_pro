from django.shortcuts import render
from django.http import HttpResponse
from .models import School
# Create your views here.

def Home(request):
    school = School.objects.all()
    context = {
        'school': school
    }
    return render(request,'home.html', context)
    