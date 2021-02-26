from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import School
from .forms import Schoolform
# Create your views here.

def Home(request):
    school = School.objects.all()
    context = {
        'school': school
    }
    return render(request,'home.html', context)

def create_school(request):
    if request.method == "GET":
        form = Schoolform()
        context = {
            'form':form
            }
        return render(request, 'create_school.html', context)
    else:
        form = Schoolform(request.POST, request.FILES)
        context = {
                'form':form
                }
        form.save()
        return redirect('home')

def update_school(request, pk):
    school = get_object_or_404(School,pk=pk)
    if request.method == 'GET':
        form = Schoolform(instance=school)
        return render(request, 'update_school.html', {'form': form, 'school': school})
    else:
        form = Schoolform(request.POST, request.FILES, instance=school)
        form.save()
        return redirect('home')
    